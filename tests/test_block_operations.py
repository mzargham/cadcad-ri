from pytest import fixture, raises

from cadcad.dynamics import Block, block
from cadcad.points import Point
from cadcad.spaces import Space, space

def test_valid_wiring(first_block: Block, second_block: Block, experiment_params: dict) -> None:
    pass

def test_invalid_wiring(first_block: Block, experiment_params: dict) -> None:
    pass