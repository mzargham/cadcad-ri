import pytest

from cadcad.dynamics import Block, block
from cadcad.points import Point
from cadcad.spaces import Space, space

# pylint: disable=line-too-long, missing-function-docstring, missing-class-docstring, invalid-name, redefined-outer-name  # noqa: E501

def test_valid_wiring(first_block: Block, second_block: Block, experiment_params: dict) -> None:
    pass


def test_invalid_wiring(first_block: Block, experiment_params: dict) -> None:
    pass


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
