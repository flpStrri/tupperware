from tupperware.maybe import Nothing


def test_should_not_return_container_inner_value_when_calculating_nothing_str_representation():
    nothing = Nothing()
    assert str(nothing) == "<Nothing>"
