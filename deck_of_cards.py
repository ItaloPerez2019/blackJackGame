class Card: 
	def __init__(self, value, suit ):
		self.value  = value 
		self.suit = suit


	def __repr__(self):
		return f" {self.value} and {self.suit}"

class Deck:
	def __init__(self):
		suits = ['Heart', 'Diamonds', 'Clubs', 'Spades']
		values = ['A','2','3','4','5','6','7','8','9','10' ,'J' ,'Q','K']
		self.cards =[ Card(value,suit) for suit in suits for value in values]
		''' avoid to write code this way'''
		# self.cards = []
		# for suit in suits: 
		# 	for value in values: 
		# 		self.vards.append(Card(value.suit))
		print (self.cards)


	def __repr__(self):
		return f"Deck of {self.count()} cards"

	def count(self):
		return len(self.cards)


d = Deck()
print(d)