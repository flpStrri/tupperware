from tupperware.either import Left, Right


def test_should_return_inner_value_when_checking_value_given_right():
    assert Right(2).value == 2


def test_should_return_inner_value_when_checking_value_given_left():
    assert Left(2).value == 2
