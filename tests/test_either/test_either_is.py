from tupperware.either import Left, Right


def test_should_return_true_when_checking_if_right_is_right_type_given_right():
    assert Right(2).is_right is True


def test_should_return_false_when_checking_if_right_is_left_type_given_right():
    assert Right(2).is_left is False


def test_should_return_true_when_checking_if_left_is_left_type_given_left():
    assert Left(2).is_left is True


def test_should_return_false_when_checking_if_left_is_right_type_given_left():
    assert Left(2).is_right is False
