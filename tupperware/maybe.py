from abc import ABCMeta, abstractmethod
from typing import (
    Any,
    Callable,
    Generic,
    NoReturn,
    Optional,
    TypeVar,
    Union,
)
from typing_extensions import final

from tupperware.primitives.container import Container

# Definitions:
_ValueType = TypeVar("_ValueType", covariant=True)
_NewValueType = TypeVar("_NewValueType")


class Maybe(
    Container, Generic[_ValueType], metaclass=ABCMeta,
):
    """Encapsulates an optional value.

    The Maybe type encapsulates an optional value. A value of type
    Maybe a either contains a value (represented as Just a), or it is
    empty (represented as Nothing).
    """

    _inner_value: Optional[_ValueType]

    @abstractmethod
    def map(
        self, function: Callable[[_ValueType], Optional[_NewValueType]],
    ) -> "Maybe[_NewValueType]":
        """
        Composes not empty container with a pure function.
        """
        raise NotImplementedError

    @abstractmethod
    def bind(
        self, function: Callable[[_ValueType], "Maybe[_NewValueType]"],
    ) -> "Maybe[_NewValueType]":
        """
        Composes not empty container with a function that returns a container.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def is_just(self) -> bool:
        raise NotImplementedError

    @property
    @abstractmethod
    def is_nothing(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def value_or(self, default_value: _NewValueType,) -> Union[_ValueType, _NewValueType]:
        """
        Get value from successful container or default value from failed one.
        """
        raise NotImplementedError

    @classmethod
    def from_value(cls, inner_value: Optional[_ValueType],) -> "Maybe[_ValueType]":
        """
        Creates new instance of ``Maybe`` container based on a value.
        """
        if inner_value is None:
            return _Nothing(inner_value)
        return _Just(inner_value)

    @abstractmethod
    def __or__(
        self, function: Callable[[_ValueType], "Maybe[_NewValueType]"]
    ) -> "Maybe[_NewValueType]":
        """
        Use | as operator for bind.
        """
        raise NotImplementedError


@final
class _Nothing(Maybe[Any]):
    """Represents an empty state."""

    _inner_value: None

    def __init__(self, inner_value: None = None) -> None:
        super().__init__(None)

    def map(self, function):
        return self

    def bind(self, function):
        return self

    @property
    def is_just(self):
        return False

    @property
    def is_nothing(self):
        return True

    def value_or(self, default_value):
        return default_value

    def __str__(self):
        """Custom ``str`` definition without the state inside."""
        return "<Nothing>"

    def __or__(self, function):
        return self.bind(function)


@final
class _Just(Maybe[_ValueType]):
    """
    Represents a calculation which has succeeded and contains the value.
    """

    _inner_value: _ValueType

    def __init__(self, inner_value: _ValueType) -> None:
        super().__init__(inner_value)

    def map(self, function):
        return Maybe.from_value(function(self._inner_value))

    def bind(self, function):
        return function(self._inner_value)

    @property
    def is_just(self):
        return True

    @property
    def is_nothing(self):
        return False

    def value_or(self, default_value):
        return self._inner_value

    def __or__(self, function):
        return self.bind(function)


def Just(inner_value: Optional[_ValueType]) -> Maybe[_ValueType]:
    return Maybe.from_value(inner_value)


def Nothing(inner_value: None = None) -> Maybe[NoReturn]:
    return _Nothing(inner_value)
