
@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fib(n, result):
    """testing fib function"""
    from series import fib_func
    assert fib_func(n) == result 
