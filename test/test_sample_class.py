from project_name.sample_module import SampleClass


def test_simple_method():
    # Given
    a = 1
    b = 2

    # When
    result = SampleClass.sample_method(a, b)

    # Then
    assert result == 3
