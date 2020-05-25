from tupperware.either import Either, Left, Right


def test_should_return_right_when_creating_either_from_value():
    assert Either.from_value(2) == Right(2)


def test_should_return_right_when_creating_either_from_failure():
    assert Either.from_failure("error") == Left("error")
