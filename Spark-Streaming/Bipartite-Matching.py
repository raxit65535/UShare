from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from kafka import KafkaProducer
# from pyspark.sql.functions import expr
from pyspark.streaming.kafka import KafkaUtils
import sys
from datetime import datetime
from math import radians, cos, sin, asin, sqrt
# from configparser import ConfigParser


def kafkaSink(matched_stats):
    producer = KafkaProducer(bootstrap_servers="localhost:9092")
    # producer = KafkaProducer(bootstrap_servers = "10.0.0.4:9092, 10.0.0.5:9092, 10.0.0.10:9092")
    print(matched_stats)
    producer.send('matched_stats', matched_stats.encode('utf8'))
    producer.flush()


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """

    # lonlat1 = lonlat1.strip("()").split(",")
    # lonlat2 = lonlat2.strip("()").split(",")

    lon1 = float(lon1)
    lat1 = float(lat1)
    lon2 = float(lon2)
    lat2 = float(lat2)
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r


def format_message_matched(ride_request_id, pickup_loc, drop_off_loc, water_mark_rider, driver_id, driver_loc, water_mark_driver, distance, now_timestamp):
    str_fmt = "{};{};{};{};{};{};{};{};{}"
    message = str_fmt.format(ride_request_id, pickup_loc, drop_off_loc, water_mark_rider,
                             driver_id, driver_loc, water_mark_driver, distance, now_timestamp)
    # print(message)
    return message


def format_message_driver(driver_id, driver_loc, timestamp):
    str_fmt = "{};{};{}"
    message = str_fmt.format(driver_id, driver_loc, timestamp)
    # print(message)
    return message

def format_match_stats(total_ride_req, matched_riders, unmatched_riders, total_drivers, unmatched_driver, timestamp):
    str_fmt = "{};{};{};{};{};{}"
    message = str_fmt.format(total_ride_req, matched_riders, total_drivers, unmatched_riders, unmatched_driver, timestamp)
    # print(message)
    return message


def process_union(rdd):
    matched_list = dict()
    matched_driver = dict()

    total_ride_req = dict()
    total_driver = dict()

    sink_match = list()
    sink_driver = list()

    unmatched_rider_list = []
    unmatched_driver_list = []
    # print("raxit start")
    for line in rdd:

        rider, driver = line[1]
        rider = rider.split(";")
        driver = driver.split(";")

        ride_pickup = rider[1].strip("()").split(",")
        driver_loc = driver[1].strip("()").split(",")
        ride_long = ride_pickup[0]
        ride_lat = ride_pickup[1]
        driver_long = driver_loc[0]
        driver_lat = driver_loc[1]

        if rider[0] not in total_ride_req:
            total_ride_req[rider[0]] = "new"

        if driver[0] not in total_driver:
            total_driver[driver[0]] = "new"

        if rider[0] not in matched_list and driver[0] not in matched_driver:
            # print("not yet matched")
            distance = haversine(ride_long, ride_lat, driver_long, driver_lat)
            if distance > 1 and distance < 3:
                # print("herversine true, adding the value")
                matched_list[rider[0]] = driver[0]
                kafka_matched_sink = format_message_matched(
                    rider[0], rider[1], rider[2], rider[3], driver[0], driver[1], driver[2], distance, str(datetime.now()))
                sink_match.append(kafka_matched_sink)
                kafka_driver_sink = format_message_driver(
                    driver[0], rider[2], str(datetime.now()))
                sink_driver.append(kafka_driver_sink)
                matched_driver[driver[0]] = ""

        # print("raxit stop", line[1])
    for key in matched_list:
        # print("raxit: iterating key", key)
        if key not in total_ride_req:
            # print("raxit:appending key")
            unmatched_rider_list.append(key)

    for key in matched_driver:
        if key not in total_driver:
            unmatched_driver_list.append(key)


    if len(matched_list) != 0:
        print("inserting value:", len(matched_list))
        matched_stats = format_match_stats(len(total_ride_req), len(matched_list), len(unmatched_rider_list), len(total_driver), len(unmatched_driver_list), str(datetime.now())) 
        kafkaSink(matched_stats)
    
    # print("total number of ride request in a window: ", len(total_ride_req))
    # print("Ride requests matched with driver in a window: ", len(matched_list))
    # print("total number of driver active in the window: ", len(total_driver))
    # print("number of drivers matched with rider in the window: ", len(matched_driver))

    # print(len(total_ride_req), len(matched_list))
    # print(len(total_driver), len(matched_driver))
    # print(len(sink_match), len(sink_driver))


def main():

    sparkContext = SparkContext(appName='Bipartite-Matching')
    sparkContext.setLogLevel('ERROR')
    sparkStreamingContext = StreamingContext(sparkContext, 1)
    # kafka_params = config('kafka')

    # create DStream that reads from kafka topic
    spark_kafka_driver_Stream = KafkaUtils.createDirectStream(sparkStreamingContext, ['driver_topic'],
                                                              # {'metadata.broker.list': '10.0.0.4:9092, 10.0.0.5:9092, 10.0.0.10:9092'})
                                                              {'metadata.broker.list': 'localhost:9092'})
    spark_kafka_rider_stream = KafkaUtils.createDirectStream(sparkStreamingContext, ['rider_topic'],
                                                             #  {'metadata.broker.list': '10.0.0.4:9092, 10.0.0.5:9092, 10.0.0.10:9092'})
                                                             {'metadata.broker.list': 'localhost:9092'})


    driver_window = spark_kafka_driver_Stream.window(1)
    rider_window = spark_kafka_rider_stream.window(2)

    union_rdd = rider_window.leftOuterJoin(driver_window)

    print(haversine(-73.93758392333984, 40.75828170776367, -
                    73.93763732910156, 40.758270263671875))
    union_rdd = union_rdd.foreachRDD(lambda rdd: rdd.foreachPartition(process_union))
    sparkStreamingContext.start()
    sparkStreamingContext.awaitTermination()


if __name__ == '__main__':
    main()
