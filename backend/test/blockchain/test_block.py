from backend.blockchain.block import Block, GENESIS_DATA


def test_mine_block():
    last_block = Block.genesis()
    data = 'test data'
    block = Block.mine_block(last_block, data)

    assert isinstance(block, Block)
    assert block.data == data


def test_genesis():
    genesis = Block.genesis()

    assert isinstance(genesis, Block)
    for key, value in GENESIS_DATA.items():
       getattr(genesis, key) == value


