from functools import partial
from operator import add

from tupperware.either import Left, Right


def test_should_return_right_when_mapping_given_right():
    right_one = Right(1)
    assert right_one.map(partial(add, 1)) == Right(2)


def test_should_return_the_same_left_when_mapping_given_left():
    left_one = Left(1)
    assert left_one.map(partial(add, 1)) == left_one
