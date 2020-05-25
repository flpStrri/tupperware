from random import choice
from typing import Callable

from tupperware.either import Either, Left, Right


def test_should_return_right_when_binding_right_given_function_returning_right():
    right_one = Right(1)

    right_add_one: Callable[[int], Either[int, int]] = lambda to_sum: Right(to_sum + 1)

    assert right_one.bind(right_add_one) == Right(2)
    assert right_one | right_add_one == Right(2)


def test_should_return_left_when_binding_right_given_function_returning_left():
    right_one = Right(1)

    left_add_one: Callable[[int], Either[int, int]] = lambda to_sum: Left(to_sum + 1)

    assert right_one.bind(left_add_one) == Left(2)
    assert right_one | left_add_one == Left(2)


def test_should_return_the_same_left_when_binding_left_given_function_returning_right_or_left():
    left_one = Left(1)

    add_one: Callable[[int], Either[int, int]] = lambda to_sum: choice(
        [Right(to_sum + 1), Left(to_sum + 1)]
    )

    assert left_one.bind(add_one) == left_one
    assert left_one | add_one == left_one
