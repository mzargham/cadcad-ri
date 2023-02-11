import pytest
from cadcad.spaces import space, Space
from cadcad.dynamics import block, Block
from cadcad.points import Point

@pytest.fixture()
def first_space() -> type:
    @space
    class FirstSpace:
        dim1: int
        dim2: int

    return FirstSpace


@pytest.fixture()
def second_space() -> type:
    @space
    class SecondSpace:
        pickles: float
        skittles: float

    return SecondSpace


@pytest.fixture()
def third_space() -> type:
    @space
    class ThirdSpace:
        candy: str
        popcorn: str

    return ThirdSpace


@pytest.fixture()
def first_block(first_space: Space, second_space: Space) -> Block:
    @block
    def first_space_to_second_space(domain: Point[first_space]) -> Point[second_space]:
        return Point(second_space, {"pickles": 1.0, "skittles": 2.0})

    return first_space_to_second_space


@pytest.fixture()
def second_block(second_space: Space, third_space: Space) -> Block:
    @block
    def second_space_to_third_space(
        domain: Point[second_space],
    ) -> Point[third_space]:
        return Point(third_space, {"candy": "yum", "popcorn": "ew"})

    return second_space_to_third_space


@pytest.fixture()
def first_block_with_invalid_output(
    first_space: Space, second_space: Space, third_space: Space
) -> Block:
    @block
    def first_space_to_second_space(domain: Point[first_space]) -> Point[second_space]:
        return Point(third_space, {"candy": "yum", "popcorn": "ew"})

    return first_space_to_second_space


@pytest.fixture(scope="module")
def experiment_params() -> dict:
    return {"iteration_n": 1, "steps": 1}