from tupperware.maybe import Just, Maybe, Nothing


def test_should_return_just_when_creating_maybe_from_value_given_not_none():
    assert Maybe.from_value(2) == Just(2)


def test_should_return_nothing_when_creating_maybe_from_value_given_none():
    assert Maybe.from_value(None) == Nothing()
