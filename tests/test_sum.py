from pyo3_demo import sum_as_string

def test_add():
    a, b = 1, 2
    c = sum_as_string(a, b)
    assert c == "3"
