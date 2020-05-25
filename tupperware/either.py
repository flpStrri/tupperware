from abc import ABCMeta, abstractmethod
from typing import (
    Any,
    Callable,
    Generic,
    TypeVar,
    Union,
)
from typing_extensions import final

from tupperware.primitives.container import Container

# Definitions:

_ValueType = TypeVar("_ValueType", covariant=True)
_NewValueType = TypeVar("_NewValueType")
_ErrorType = TypeVar("_ErrorType", covariant=True)
_NewErrorType = TypeVar("_NewErrorType")
_InnerValue = TypeVar("_InnerValue", bound="Either")
_EitherExit = TypeVar("_EitherExit")


class Either(
    Container, Generic[_ValueType, _ErrorType], metaclass=ABCMeta,
):
    """Encapsulates a successful or failed computation.

    The Either type encapsulates an computation return value. A value
    of type Either a either contains a successful computation value
    (represented as Right a), or a a failed computation value
    (represented as Left a).
    """

    _inner_value: Union[_ValueType, _ErrorType]

    @abstractmethod
    def map(
        self, function: Callable[[_ValueType], _NewValueType],
    ) -> "Either[_NewValueType, _ErrorType]":
        """
        Composes successful container with a pure function.
        """
        raise NotImplementedError

    @abstractmethod
    def bind(
        self, function: Callable[[_ValueType], "Either[_NewValueType, _ErrorType]"],
    ) -> "Either[_NewValueType, _ErrorType]":
        """
        Composes successful container with a function that returns a container.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def is_right(self) -> bool:
        raise NotImplementedError

    @property
    @abstractmethod
    def is_left(self) -> bool:
        raise NotImplementedError

    @property
    @abstractmethod
    def value(self) -> Union[_ValueType, _ErrorType]:
        raise NotImplementedError

    @classmethod
    def from_value(cls, inner_value: _NewValueType,) -> "Either[_NewValueType, Any]":
        return Right(inner_value)

    @classmethod
    def from_failure(cls, inner_value: _NewErrorType,) -> "Either[Any, _NewErrorType]":
        return Left(inner_value)

    @abstractmethod
    def __or__(
        self, function: Callable[[_ValueType], "Either[_NewValueType, _ErrorType]"],
    ) -> "Either[_NewValueType, _ErrorType]":
        """
        Use | as operator for bind.
        """
        raise NotImplementedError


@final
class _Left(Either[Any, _ErrorType]):
    """
    Represents a failed computation.
    """

    _inner_value: _ErrorType

    def __init__(self, inner_value: _ErrorType) -> None:
        super().__init__(inner_value)

    def map(self, function):
        return self

    def bind(self, function):
        return self

    @property
    def is_right(self):
        return False

    @property
    def is_left(self):
        return True

    @property
    def value(self) -> _ErrorType:
        return self._inner_value

    def __or__(self, function):
        return self.bind(function)


@final
class _Right(Either[_ValueType, Any]):
    """
    Represents a succeeded computation.
    """

    _inner_value: _ValueType

    def __init__(self, inner_value: _ValueType) -> None:
        super().__init__(inner_value)

    def map(self, function):
        return Right(function(self._inner_value))

    def bind(self, function):
        return function(self._inner_value)

    @property
    def is_right(self):
        return True

    @property
    def is_left(self):
        return False

    @property
    def value(self) -> _ValueType:
        return self._inner_value

    def __or__(self, function):
        return self.bind(function)


def Right(inner_value: _NewValueType,) -> Either[_NewValueType, Any]:
    return _Right(inner_value)


def Left(inner_value: _NewErrorType,) -> Either[Any, _NewErrorType]:
    return _Left(inner_value)


def either(
    left_mapper: Callable[[_InnerValue], _EitherExit],
    right_mapper: Callable[[_InnerValue], _EitherExit],
    container: _InnerValue,
) -> _EitherExit:
    return left_mapper(container) if container.is_left else right_mapper(container)
