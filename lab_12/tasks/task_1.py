def generate_fibonacci(numb=100):
    if not isinstance(numb, int) or numb < 1:
        raise RuntimeError
    n = numb if numb <= 100 and numb>=1 else 100
    value = 0
    yield value
    i = 1
    fibonaci = 1
    while i < n:
        yield fibonaci
        value, fibonaci = fibonaci, value + fibonaci
        i += 1


if __name__ == '__main__':
    assert list(generate_fibonacci(1)) == [0]
    assert list(generate_fibonacci(2)) == [0, 1]
    assert sum(generate_fibonacci(10)) == 88
    ii = 0
    for ii in generate_fibonacci():
        pass
    assert ii == 218922995834555169026
    try:
        generate_fibonacci(0)
    except Exception as exc:
        assert isinstance(exc, RuntimeError)
