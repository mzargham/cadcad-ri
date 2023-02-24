import pytest

from cadcad.dynamics import Block, block
from cadcad.points import Point
from cadcad.spaces import Space, space
from cadcad.errors import BlockInputError

def test_valid_block_domains(first_block: Block) -> None:
    """
    Test that the domains of a block are a list of spaces
    """
    domains = first_block.domains
    assert type(domains) == list
    for domain in domains:
        assert type(domain) == Space

def test_valid_block_codomains(first_block: Block) -> None:
    """
    Test that the codomains of a block are a list of spaces
    """
    codomains = first_block.codomains
    assert type(codomains) == list
    for codomain in codomains:
        assert type(codomain) == Space

def test_SISO_block_constructor_annotations(first_space:Space, second_space:Space) -> None:
    """
    Test that the constructor of a block is annotated with points in the domain and codomain respectively
    """
    @block
    def first_space_to_second_space(args: Point[first_space]) -> Point[second_space]:
        return Point(second_space, {"pickles": 1.0, "skittles": 2.0})
    
    # copilot's tests (need to be revisited by emanuel)
    #assert first_space_to_second_space.__annotations__ == {"domain": Point[first_space], "return": Point[second_space]}
    
    # Z's tests
    assert first_space_to_second_space.domain == [first_space]
    assert first_space_to_second_space.codomain == [second_space]

def test_MISO_block_constructor_annotations(first_space:Space, second_space:Space, third_space:Space) -> None:
    """
    Test that the constructor of a block is annotated with points in the domain and codomain respectively
    """
    @block
    def first_space_to_second_space(arg1: Point[first_space], arg2: Point[second_space]) -> Point[third_space]:
        return Point(third_space, {"candy": "skittles", "popcorn": "salted with butter"})
    
    # copilot's tests (need to be revisited by emanuel)
    #assert first_space_to_second_space.__annotations__ == {"domain": Point[first_space], "return": Point[second_space]}
    
    # Z's tests
    assert first_space_to_second_space.domain == [first_space, second_space]
    assert first_space_to_second_space.codomain == [third_space]


def test_block_constructor_bad_type_annotations(first_space:Space, second_space:Space) -> None:
    """
    Test that the constructor of a block is annotated with points in the domain and codomain respectively
    """

    with pytest.raises(BlockInputError):   
        @block
        def first_space_to_second_space(args: first_space) -> Point[second_space]:
            return Point(second_space, {"pickles": 1.0, "skittles": 2.0})

    with pytest.raises(BlockInputError):   
        @block
        def first_space_to_second_space(args: Point[first_space]) -> second_space:
            return Point(second_space, {"pickles": 1.0, "skittles": 2.0})

    
    