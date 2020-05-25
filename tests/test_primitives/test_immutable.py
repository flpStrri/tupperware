from copy import copy, deepcopy

from pytest import raises

from tupperware.primitives.container import Container
from tupperware.exceptions import ImmutableStateError


def test_immutable_should_not_mutate_inner_value():
    immutable_container = Container(1)
    with raises(Exception) as exception_info:
        immutable_container._inner_value = 2
    assert exception_info.type == ImmutableStateError


def test_immutable_should_not_delete_inner_value():
    immutable_container = Container(1)
    with raises(Exception) as exception_info:
        del immutable_container._inner_value
    assert exception_info.type == ImmutableStateError


def test_immutable_container_should_not_have_other_attributes():
    immutable_container = Container(1)
    with raises(Exception) as exception_info:
        immutable_container.other = 2
    assert exception_info.type == ImmutableStateError


def test_immutable_copies_can_be_the_same_thing():
    immutable_container = Container(1)
    assert immutable_container is copy(immutable_container)
    assert immutable_container is deepcopy(immutable_container)
