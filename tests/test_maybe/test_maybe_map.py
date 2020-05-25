from functools import partial
from operator import add
from typing import Callable, Mapping, Optional
from tupperware.maybe import Just, Nothing


def test_should_return_just_when_mapping_given_just_and_a_func_that_return_value():
    maybe_one = Just(1)
    assert maybe_one.map(partial(add, 1)) == Just(2)


def test_should_return_nothing_when_mapping_given_nothing():
    maybe_nothing = Nothing()
    assert maybe_nothing.map(partial(add, 1)) == Nothing()


def test_should_return_nothing_when_mapping_given_just_and_a_func_that_returns_none():
    just_boris = Just({"name": "Boris"})
    get_age: Callable[[Mapping], Optional[int]] = lambda mapping: mapping.get("age")

    assert just_boris.map(get_age).map(partial(add, 1)) == Nothing()
