from cadcad.dynamics import Block, block
from cadcad.points import Point

def series(blocks: list[Block]) -> Block:
    """Wires a list of blocks in series and returns a block that represents the wiring,
    requires each block's codomain to match the next block's domain.

    Input and output types are inferred from the domain and codomain of the blocks.
    
    Arguments
    ----------
    blocks : list[Block]
        List of blocks to be wired in series

    Returns
    -------
    Block
        Block that represents the wiring of the blocks in series
    """
    n = len(blocks)
    for i in range(n - 1):
        if blocks[i].codomain != blocks[i + 1].domain:
            raise WiringError(
                f"Block {i} codomain {blocks[i].codomain} does not match block {i + 1} domain {blocks[i + 1].domain}"
            )

    domains = blocks[0].domain
    if type(domains) is not list:
        domains = [domains]
    
    input_types = [Point[Domain] for Domain in domains]

    codomains = blocks[-1].codomain
    if type(codomains) is not list:
        codomains = [codomains]

    output_types = [Point[Codomain] for Codomain in codomains]

    @block
    def series_block(*inputs: input_types,
        parameters: Dict[str, int] =  {block.__name__:block.parameters for block in blocks},
    ) -> output_types:
        """_summary_

        Parameters
        ----------
        inputs : List[Point[Space]]
            _description_
        parameters : Dict[str, int]
            _description_

        Returns
        -------
        List[Point[Space]]
            _description_
        """
       
        ouputs = inputs
        for block in blocks:
            outputs = block(*outputs, parameters=parameters[block.__name__])

        return outputs

    return series_block