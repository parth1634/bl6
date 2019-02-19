# bl6


# Example
    msg1 = Message("simple message")
    msg2 = Message("with a sender and receiver", "Alice", "Bob")
    
    # each of the above now has a hashed payload, link them by adding to a block

    block1 = Block()
    block1.add_message(msg1)
    block1.add_message(msg2)

    # or using the constructor

    block1 = Block(msg1, msg2)

    # messages are now fully hashed and linked, msg2 depends on msg1, tampering can be detected

    block2 = Block()
    block2.add_message(Message("just need a second block for an example"))

    # now link the blocks together

    chain = Blockchain()
    chain.add_block(block1)
    chain.add_block(block2)

    # now the blocks are linked, block2 depends on block1