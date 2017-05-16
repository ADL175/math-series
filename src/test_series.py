import pytest

FIB_TABLE = [(0,0), (1,1), (2,1), (3,2), (4,3), (5,5), (6,8), (7,13)]

LUC_TABLE = [(0,2), (1,1), (2,3), (3,4), (4,7), (5,11), (6,18), (7,29)]

@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fib(n, result):
    """testing fib function"""
    from series import fib_func
    assert fib_func(n) == result 


@pytest.mark.parametrize('n, result', LUC_TABLE)
def test_lucas(n, result):
    """testing lucas function"""
    from series import lucas_func
    assert lucas_func(n) == result 