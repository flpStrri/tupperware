from dataclasses import dataclass
from typing import Callable, List, Optional
from unittest.mock import MagicMock

from tupperware.either import Either, Left, either, Right


@dataclass
class ApplicationReturnTest:
    errors: Optional[List[str]] = None
    sum: Optional[int] = None


def test_should_return_exit_type_from_left_mapper_when_calling_either_with_mapping_functions_given_left_container():
    left_container = Left(["error one", "error two"])

    left_mapper: Callable[[Either[int, List[str]]], ApplicationReturnTest] = MagicMock(
        return_value=ApplicationReturnTest(errors=["error one", "error two"])
    )
    right_mapper: Callable[[Either[int, List[str]]], ApplicationReturnTest] = MagicMock()
    assert either(
        left_mapper=left_mapper, right_mapper=right_mapper, container=left_container,
    ) == ApplicationReturnTest(sum=None, errors=["error one", "error two"])


def test_should_return_exit_type_from_right_mapper_when_calling_either_with_mapping_functions_given_right_container():
    right_container = Right(1)

    left_mapper: Callable[[Either[int, List[str]]], ApplicationReturnTest] = MagicMock()
    right_mapper: Callable[[Either[int, List[str]]], ApplicationReturnTest] = MagicMock(
        return_value=ApplicationReturnTest(sum=1)
    )
    assert either(
        left_mapper=left_mapper, right_mapper=right_mapper, container=right_container,
    ) == ApplicationReturnTest(sum=1, errors=None)
