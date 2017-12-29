from enum import Enum, auto


class Card:
	class CardType(Enum):
		Treasure = auto()
		Action = auto()
		Reaction = auto()
		Attack = auto()
		Victory = auto()
		Curse = auto()

	prevent_attack = False

	def __init__(self, name, cost, cardtype, value, coin, action, buy, draw, owner):
		self.__name = name
		self.__cost = cost
		self.__coin = coin
		self.__type = cardtype
		self.__action = action
		self.__buy = buy
		self.__draw = draw
		self.__value = value
		self.__owner = owner

	def play(self):
		self.__owner.add_actions(self.__action)
		self.__owner.add_buys(self.__buy)
		self.__owner.add_purchase_power(self.__coin)
		self.__owner.draw_cards(self.__draw)
		self.effect()

	def effect(self):
		# This is here so that 'special' cards can override this function so that unique card effects can happen.
		pass

	def passive(self):
		# This is here so that 'special' cards can override this function so that unique card passives can happen.
		pass

	def get_name(self):
		return self.__name

	def get_type(self):
		return self.__type

	def get_cost(self):
		return self.__cost

	def set_owner(self, owner):
		self.__owner = owner

	def get_owner(self):
		return self.__owner

	def identify(self):
		return self.__name + ", " + str(self.__type) + ", " + str(self.__cost)

	def __get_index_not_self(self):
		result = -1
		for c in self._Card__owner.get_hand().get_supply():
			if c != self:
				result = self._Card__owner.get_hand().get_supply().index(c)
		return result