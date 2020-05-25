from tupperware.maybe import Just, Nothing


def test_should_return_true_when_checking_if_just_is_just_type_given_just():
    assert Just(2).is_just is True


def test_should_return_false_when_checking_if_just_is_nothing_type_given_just():
    assert Just(2).is_nothing is False


def test_should_return_true_when_checking_if_nothing_is_nothing_type_given_nothing():
    assert Nothing().is_nothing is True


def test_should_return_false_when_checking_if_nothing_is_just_type_given_nothing():
    assert Nothing().is_just is False
