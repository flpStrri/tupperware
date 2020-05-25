from tupperware.primitives.container import Container


def test_container_should_stringify():
    assert str(Container(1)) == "<Container: 1>"


def test_container_should_hash():
    assert hash(Container(1))


def test_container_should_not_be_equal_to_content():
    assert Container(1) != 1
