from random import choice
from typing import Callable

from tupperware.maybe import Just, Maybe, Nothing


def test_should_return_just_when_binding_just_given_function_returning_just():
    just_one = Just(1)

    just_add_one: Callable[[int], Maybe[int]] = lambda to_sum: Just(to_sum + 1)

    assert just_one.bind(just_add_one) == Just(2)
    assert just_one | just_add_one == Just(2)


def test_should_return_nothing_when_binding_just_given_function_returning_nothing():
    just_one = Just(1)

    make_nothing: Callable[[int], Maybe[int]] = lambda _: Nothing()

    assert just_one.bind(make_nothing) == Nothing()
    assert just_one | make_nothing == Nothing()


def test_should_return_the_same_nothing_when_binding_nothing_given_function_returning_just_or_nothing():
    nothing = Nothing()

    just_add_one: Callable[[int], Maybe[int]] = lambda to_sum: choice([Just(to_sum + 1), Nothing()])

    assert nothing.bind(just_add_one) == Nothing()
    assert nothing | just_add_one == Nothing()
