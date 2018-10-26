def test_division_entera():
    num1 = 10
    num2 = 3

    my_div = num1 // num2
    print(my_div)
    assert 3 == my_div

def test_division_exacta():
    import sys
    print(sys.version)

    import platform
    print(platform.python_version())

    num1 = 10.
    num2 = 3

    my_div = num1 / num2
    print(my_div)
    assert 3 == my_div