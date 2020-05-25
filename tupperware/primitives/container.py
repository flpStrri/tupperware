from abc import ABCMeta
from typing import Any

from tupperware.primitives.immutable import Immutable


class Container(Immutable, metaclass=ABCMeta):
    """Utility class to provide all needed magic methods to the context."""

    __slots__ = ("_inner_value",)
    _inner_value: Any

    def __init__(self, inner_value) -> None:
        """
        Wraps the given value in the Container.
        'value' is any arbitrary value of any type including functions.
        """
        object.__setattr__(self, "_inner_value", inner_value)

    def __str__(self) -> str:
        return "<{0}: {1}>".format(self.__class__.__qualname__.strip("_"), str(self._inner_value),)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(self, type(other)):
            return False
        return self._inner_value == other._inner_value

    def __hash__(self) -> int:
        return hash(self._inner_value)
