from typing import Any, Dict, NoReturn

from tupperware.exceptions import ImmutableStateError


class Immutable(object):
    """
    Helper type for objects that should be immutable.
    When applied, each instance becomes immutable.
    Nothing can be added or deleted from it.
    """

    def __copy__(self) -> "Immutable":
        """Returns it self."""
        return self

    def __deepcopy__(self, memo: Dict[Any, Any]) -> "Immutable":
        """Returns it self."""
        return self

    def __setattr__(self, attr_name: str, attr_value: Any) -> NoReturn:
        """Makes inner state of the containers immutable for modification."""
        raise ImmutableStateError()

    def __delattr__(self, attr_name: str) -> NoReturn:
        """Makes inner state of the containers immutable for deletion."""
        raise ImmutableStateError()
