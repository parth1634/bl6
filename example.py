from blockchain import Message, Block, Blockchain
import pickle

B1 = Block()
B1.add_message(Message("This is the 1st message"))
B1.add_message(Message("2nd message", "Alice", "Bob"))
B1.add_message(Message("3rd message", "Bob", "Alice"))
B1.seal()

B2 = Block()
B2.add_message(Message("4th message"))
B2.add_message(Message("5th message", "Eve", "Steve"))
B2.seal()

B3 = Block()
B3.add_message(Message("6th message"))
B3.add_message(Message("7th message", "Me", "Everyone"))
B3.seal()


chain = Blockchain()
chain.add_block(B1)
chain.add_block(B2)
chain.add_block(B3)

print("Validating blockchain...")
chain.validate()   

print("Serializing...")
pickle.dump(chain, open('chain.p', 'wb'))

print("Deserializing and validating...")
chain2 = pickle.load(open('chain.p', 'rb'))
chain2.validate()

print("Serializing for tampering...")
pickle.dump(chain2, open('chain.p', 'wb'))

print("Hostile tampering...")
tampered = pickle.load(open('chain.p', 'rb'))
tampered.blocks[2].messages[1].data = "7th message"  
pickle.dump(tampered, open('chain.p', 'wb'))

print("Deserializing tampered chain and validating...")
chain3 = pickle.load(open('chain.p', 'rb'))
chain3.validate()      