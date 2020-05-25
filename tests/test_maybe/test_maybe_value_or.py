from tupperware.maybe import Just, Nothing


def test_should_return_internal_value_when_getting_value_from_just():
    assert Just(1).value_or("nothing here") == 1


def test_should_return_default_value_when_getting_value_from_nothing():
    assert Nothing().value_or("nothing here") == "nothing here"
