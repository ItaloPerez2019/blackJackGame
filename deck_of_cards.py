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
		self.cards =[ Card(va)]
