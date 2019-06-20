import builtins as _mod_builtins
import numpy.linalg as _mod_numpy_linalg

class BGLU(LU):
    '\n    Represents PLU factorization with Golub rank-one updates from\n    Bartels, Richard H. "A stabilization of the simplex method."\n    Numerische Mathematik 16.5 (1971): 414-434.\n    '
    @property
    def L(self):
        pass
    
    @property
    def U(self):
        pass
    
    __class__ = BGLU
    def __init__(self):
        '\n        Given matrix A and basis indices b, perform PLU factorization of\n        basis matrix B\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def average_solve_times(self):
        pass
    
    @property
    def bglu_time(self):
        pass
    
    @property
    def mast(self):
        pass
    
    @property
    def max_updates(self):
        pass
    
    @property
    def ops_list(self):
        pass
    
    def perform_perm(self):
        '\n        Perform individual row swaps defined in p returned by factor_lu to\n        generate final permutation indices pi\n        '
        pass
    
    @property
    def pi(self):
        pass
    
    @property
    def pit(self):
        pass
    
    @property
    def plu(self):
        pass
    
    def refactor(self, *args, **kwargs):
        pass
    
    def solve(self, *args, **kwargs):
        pass
    
    @property
    def solves(self):
        pass
    
    def update(self, *args, **kwargs):
        pass
    
    def update_basis(self):
        pass
    
    @property
    def updates(self):
        pass
    

class LU(_mod_builtins.object):
    '\n    Represents PLU factorization of a basis matrix with naive rank-one updates\n    '
    @property
    def A(self):
        pass
    
    @property
    def B(self):
        pass
    
    __class__ = LU
    def __init__(self):
        ' Given matrix A and basis indices b, form basis matrix B '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def b(self):
        pass
    
    @property
    def m(self):
        pass
    
    @property
    def n(self):
        pass
    
    def solve(self):
        '\n        Solve B @ v = q\n        '
        pass
    
    def update(self):
        ' Rank-one update to basis and basis matrix '
        pass
    

LinAlgError = _mod_numpy_linalg.LinAlgError
__all__ = _mod_builtins.list()
__builtins__ = {}
__doc__ = None
__file__ = '/home/raxit/.local/lib/python3.6/site-packages/scipy/optimize/_bglu_dense.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.optimize._bglu_dense'
__package__ = 'scipy.optimize'
def __pyx_unpickle_BGLU():
    pass

def __pyx_unpickle_Enum():
    pass

def __pyx_unpickle_LU():
    pass

__test__ = _mod_builtins.dict()
def _consider_refactor():
    '\n    This decorator records the time spent in the major BGLU\n    routines - refactor, update, and solve - in order to\n    calculate the average time required to solve a system.\n    It also forces PLU factorization of the basis matrix from\n    scratch to minimize the average solve time and to\n    accumulation of roundoff error.\n\n    Immediately after PLU factorization, the average solve time\n    will be rather high because PLU factorization is slow. For\n    some number of factor updates, the average solve time is\n    expected to decrease because the updates and solves are fast.\n    However, updates increase the compexity of the factorization,\n    so solve times are expected to increase with each update.\n    When the average solve time stops decreasing and begins\n    increasing, we perform PLU factorization from scratch rather\n    than updating. PLU factorization is also performed after the\n    maximum permitted number of updates is reached to prevent\n    further accumulation of roundoff error.\n    '
    pass

def lu_factor(a, overwrite_a, check_finite):
    "\n    Compute pivoted LU decomposition of a matrix.\n\n    The decomposition is::\n\n        A = P L U\n\n    where P is a permutation matrix, L lower triangular with unit\n    diagonal elements, and U upper triangular.\n\n    Parameters\n    ----------\n    a : (M, M) array_like\n        Matrix to decompose\n    overwrite_a : bool, optional\n        Whether to overwrite data in A (may increase performance)\n    check_finite : bool, optional\n        Whether to check that the input matrix contains only finite numbers.\n        Disabling may give a performance gain, but may result in problems\n        (crashes, non-termination) if the inputs do contain infinities or NaNs.\n\n    Returns\n    -------\n    lu : (N, N) ndarray\n        Matrix containing U in its upper triangle, and L in its lower triangle.\n        The unit diagonal elements of L are not stored.\n    piv : (N,) ndarray\n        Pivot indices representing the permutation matrix P:\n        row i of matrix was interchanged with row piv[i].\n\n    See also\n    --------\n    lu_solve : solve an equation system using the LU factorization of a matrix\n\n    Notes\n    -----\n    This is a wrapper to the ``*GETRF`` routines from LAPACK.\n\n    Examples\n    --------\n    >>> from scipy.linalg import lu_factor\n    >>> from numpy import tril, triu, allclose, zeros, eye\n    >>> A = np.array([[2, 5, 8, 7], [5, 2, 2, 8], [7, 5, 6, 6], [5, 4, 4, 8]])\n    >>> lu, piv = lu_factor(A)\n    >>> piv\n    array([2, 2, 3, 3], dtype=int32)\n    \n    Convert LAPACK's ``piv`` array to NumPy index and test the permutation \n    \n    >>> piv_py = [2, 0, 3, 1]\n    >>> L, U = np.tril(lu, k=-1) + np.eye(4), np.triu(lu)\n    >>> np.allclose(A[piv_py] - L @ U, np.zeros((4, 4)))\n    True\n    "
    pass

def lu_solve(lu_and_piv, b, trans, overwrite_b, check_finite):
    'Solve an equation system, a x = b, given the LU factorization of a\n\n    Parameters\n    ----------\n    (lu, piv)\n        Factorization of the coefficient matrix a, as given by lu_factor\n    b : array\n        Right-hand side\n    trans : {0, 1, 2}, optional\n        Type of system to solve:\n\n        =====  =========\n        trans  system\n        =====  =========\n        0      a x   = b\n        1      a^T x = b\n        2      a^H x = b\n        =====  =========\n    overwrite_b : bool, optional\n        Whether to overwrite data in b (may increase performance)\n    check_finite : bool, optional\n        Whether to check that the input matrices contain only finite numbers.\n        Disabling may give a performance gain, but may result in problems\n        (crashes, non-termination) if the inputs do contain infinities or NaNs.\n\n    Returns\n    -------\n    x : array\n        Solution to the system\n\n    See also\n    --------\n    lu_factor : LU factorize a matrix\n\n    Examples\n    --------\n    >>> from scipy.linalg import lu_factor, lu_solve\n    >>> A = np.array([[2, 5, 8, 7], [5, 2, 2, 8], [7, 5, 6, 6], [5, 4, 4, 8]])\n    >>> b = np.array([1, 1, 1, 1])\n    >>> lu, piv = lu_factor(A)\n    >>> x = lu_solve((lu, piv), b)\n    >>> np.allclose(A @ x - b, np.zeros((4,)))\n    True\n\n    '
    pass

def solve(a, b, sym_pos, lower, overwrite_a, overwrite_b, debug, check_finite, assume_a, transposed):
    "\n    Solves the linear equation set ``a * x = b`` for the unknown ``x``\n    for square ``a`` matrix.\n\n    If the data matrix is known to be a particular type then supplying the\n    corresponding string to ``assume_a`` key chooses the dedicated solver.\n    The available options are\n\n    ===================  ========\n     generic matrix       'gen'\n     symmetric            'sym'\n     hermitian            'her'\n     positive definite    'pos'\n    ===================  ========\n\n    If omitted, ``'gen'`` is the default structure.\n\n    The datatype of the arrays define which solver is called regardless\n    of the values. In other words, even when the complex array entries have\n    precisely zero imaginary parts, the complex solver will be called based\n    on the data type of the array.\n\n    Parameters\n    ----------\n    a : (N, N) array_like\n        Square input data\n    b : (N, NRHS) array_like\n        Input data for the right hand side.\n    sym_pos : bool, optional\n        Assume `a` is symmetric and positive definite. This key is deprecated\n        and assume_a = 'pos' keyword is recommended instead. The functionality\n        is the same. It will be removed in the future.\n    lower : bool, optional\n        If True, only the data contained in the lower triangle of `a`. Default\n        is to use upper triangle. (ignored for ``'gen'``)\n    overwrite_a : bool, optional\n        Allow overwriting data in `a` (may enhance performance).\n        Default is False.\n    overwrite_b : bool, optional\n        Allow overwriting data in `b` (may enhance performance).\n        Default is False.\n    check_finite : bool, optional\n        Whether to check that the input matrices contain only finite numbers.\n        Disabling may give a performance gain, but may result in problems\n        (crashes, non-termination) if the inputs do contain infinities or NaNs.\n    assume_a : str, optional\n        Valid entries are explained above.\n    transposed: bool, optional\n        If True, ``a^T x = b`` for real matrices, raises `NotImplementedError`\n        for complex matrices (only for True).\n\n    Returns\n    -------\n    x : (N, NRHS) ndarray\n        The solution array.\n\n    Raises\n    ------\n    ValueError\n        If size mismatches detected or input a is not square.\n    LinAlgError\n        If the matrix is singular.\n    LinAlgWarning\n        If an ill-conditioned input a is detected.\n    NotImplementedError\n        If transposed is True and input a is a complex matrix.\n\n    Examples\n    --------\n    Given `a` and `b`, solve for `x`:\n\n    >>> a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])\n    >>> b = np.array([2, 4, -1])\n    >>> from scipy import linalg\n    >>> x = linalg.solve(a, b)\n    >>> x\n    array([ 2., -2.,  9.])\n    >>> np.dot(a, x) == b\n    array([ True,  True,  True], dtype=bool)\n\n    Notes\n    -----\n    If the input b matrix is a 1D array with N elements, when supplied\n    together with an NxN input a, it is assumed as a valid column vector\n    despite the apparent size mismatch. This is compatible with the\n    numpy.dot() behavior and the returned result is still 1D array.\n\n    The generic, symmetric, hermitian and positive definite solutions are\n    obtained via calling ?GESV, ?SYSV, ?HESV, and ?POSV routines of\n    LAPACK respectively.\n    "
    pass

def solve_triangular(a, b, trans, lower, unit_diagonal, overwrite_b, debug, check_finite):
    "\n    Solve the equation `a x = b` for `x`, assuming a is a triangular matrix.\n\n    Parameters\n    ----------\n    a : (M, M) array_like\n        A triangular matrix\n    b : (M,) or (M, N) array_like\n        Right-hand side matrix in `a x = b`\n    lower : bool, optional\n        Use only data contained in the lower triangle of `a`.\n        Default is to use upper triangle.\n    trans : {0, 1, 2, 'N', 'T', 'C'}, optional\n        Type of system to solve:\n\n        ========  =========\n        trans     system\n        ========  =========\n        0 or 'N'  a x  = b\n        1 or 'T'  a^T x = b\n        2 or 'C'  a^H x = b\n        ========  =========\n    unit_diagonal : bool, optional\n        If True, diagonal elements of `a` are assumed to be 1 and\n        will not be referenced.\n    overwrite_b : bool, optional\n        Allow overwriting data in `b` (may enhance performance)\n    check_finite : bool, optional\n        Whether to check that the input matrices contain only finite numbers.\n        Disabling may give a performance gain, but may result in problems\n        (crashes, non-termination) if the inputs do contain infinities or NaNs.\n\n    Returns\n    -------\n    x : (M,) or (M, N) ndarray\n        Solution to the system `a x = b`.  Shape of return matches `b`.\n\n    Raises\n    ------\n    LinAlgError\n        If `a` is singular\n\n    Notes\n    -----\n    .. versionadded:: 0.9.0\n\n    Examples\n    --------\n    Solve the lower triangular system a x = b, where::\n\n             [3  0  0  0]       [4]\n        a =  [2  1  0  0]   b = [2]\n             [1  0  1  0]       [4]\n             [1  1  1  1]       [2]\n\n    >>> from scipy.linalg import solve_triangular\n    >>> a = np.array([[3, 0, 0, 0], [2, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1]])\n    >>> b = np.array([4, 2, 4, 2])\n    >>> x = solve_triangular(a, b, lower=True)\n    >>> x\n    array([ 1.33333333, -0.66666667,  2.66666667, -1.33333333])\n    >>> a.dot(x)  # Check the result\n    array([ 4.,  2.,  4.,  2.])\n\n    "
    pass

def timer():
    'process_time() -> float\n\nProcess time for profiling: sum of the kernel and user-space CPU time.'
    return 1.0

