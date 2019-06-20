__doc__ = "This module '_dop' is auto-generated with f2py (version:2).\nFunctions:\n  x,y,iwork,idid = dopri5(fcn,x,y,xend,rtol,atol,solout,iout,work,iwork,fcn_extra_args=(),overwrite_y=0,solout_extra_args=())\n  x,y,iwork,idid = dop853(fcn,x,y,xend,rtol,atol,solout,iout,work,iwork,fcn_extra_args=(),overwrite_y=0,solout_extra_args=())\n."
__file__ = '/home/raxit/.local/lib/python3.6/site-packages/scipy/integrate/_dop.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.integrate._dop'
__package__ = 'scipy.integrate'
__version__ = b'$Revision: $'
def dop853():
    "x,y,iwork,idid = dop853(fcn,x,y,xend,rtol,atol,solout,iout,work,iwork,[fcn_extra_args,overwrite_y,solout_extra_args])\n\nWrapper for ``dop853``.\n\nParameters\n----------\nfcn : call-back function\nx : input float\ny : input rank-1 array('d') with bounds (n)\nxend : input float\nrtol : input rank-1 array('d') with bounds (*)\natol : input rank-1 array('d') with bounds (*)\nsolout : call-back function\niout : input int\nwork : input rank-1 array('d') with bounds (*)\niwork : input rank-1 array('i') with bounds (*)\n\nOther Parameters\n----------------\nfcn_extra_args : input tuple, optional\n    Default: ()\noverwrite_y : input int, optional\n    Default: 0\nsolout_extra_args : input tuple, optional\n    Default: ()\n\nReturns\n-------\nx : float\ny : rank-1 array('d') with bounds (n)\niwork : rank-1 array('i') with bounds (*)\nidid : int\n\nNotes\n-----\nCall-back functions::\n\n  def fcn(x,y): return f\n  Required arguments:\n    x : input float\n    y : input rank-1 array('d') with bounds (n)\n  Return objects:\n    f : rank-1 array('d') with bounds (n)\n  def solout(nr,xold,x,y,con,icomp,[nd]): return irtn\n  Required arguments:\n    nr : input int\n    xold : input float\n    x : input float\n    y : input rank-1 array('d') with bounds (n)\n    con : input rank-1 array('d') with bounds (5 * nd)\n    icomp : input rank-1 array('i') with bounds (nd)\n  Optional arguments:\n    nd : input int, optional\n    Default: (len(con))/(5)\n  Return objects:\n    irtn : int\n"
    pass

def dopri5():
    "x,y,iwork,idid = dopri5(fcn,x,y,xend,rtol,atol,solout,iout,work,iwork,[fcn_extra_args,overwrite_y,solout_extra_args])\n\nWrapper for ``dopri5``.\n\nParameters\n----------\nfcn : call-back function\nx : input float\ny : input rank-1 array('d') with bounds (n)\nxend : input float\nrtol : input rank-1 array('d') with bounds (*)\natol : input rank-1 array('d') with bounds (*)\nsolout : call-back function\niout : input int\nwork : input rank-1 array('d') with bounds (*)\niwork : input rank-1 array('i') with bounds (*)\n\nOther Parameters\n----------------\nfcn_extra_args : input tuple, optional\n    Default: ()\noverwrite_y : input int, optional\n    Default: 0\nsolout_extra_args : input tuple, optional\n    Default: ()\n\nReturns\n-------\nx : float\ny : rank-1 array('d') with bounds (n)\niwork : rank-1 array('i') with bounds (*)\nidid : int\n\nNotes\n-----\nCall-back functions::\n\n  def fcn(x,y): return f\n  Required arguments:\n    x : input float\n    y : input rank-1 array('d') with bounds (n)\n  Return objects:\n    f : rank-1 array('d') with bounds (n)\n  def solout(nr,xold,x,y,con,icomp,[nd]): return irtn\n  Required arguments:\n    nr : input int\n    xold : input float\n    x : input float\n    y : input rank-1 array('d') with bounds (n)\n    con : input rank-1 array('d') with bounds (5 * nd)\n    icomp : input rank-1 array('i') with bounds (nd)\n  Optional arguments:\n    nd : input int, optional\n    Default: (len(con))/(5)\n  Return objects:\n    irtn : int\n"
    pass

