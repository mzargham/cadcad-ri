from pytest import fixture, raises

from cadcad.dynamics import Block, block
from cadcad.points import Point
from cadcad.spaces import Space, space

# pylint: disable=line-too-long, missing-function-docstring, missing-class-docstring, invalid-name, redefined-outer-name  # noqa: E501

def test_block_constructor(first_block: Block, first_space: Space, second_space: Space) -> None:
    assert first_block.domain == [Point[first_space]]
    assert first_block.codomain == Point[second_space]
    #assert first_block.__name__ == "first_block" #presently blocks don't have names (should they?)


def test_valid_block_input(first_space: Space, first_block: Block, experiment_params: dict) -> None:
    pass


def test_invalid_block_input(
    second_space: Space, first_block: Block, experiment_params: dict
) -> None:
    pass


def test_valid_block_output(
    first_space: Space, first_block: Block, experiment_params: dict
) -> None:
    pass


def test_invalid_block_output(
    first_space: Space, first_block_with_invalid_output: Block, experiment_params: dict
) -> None:
    pass
