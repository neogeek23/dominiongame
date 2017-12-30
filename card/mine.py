from card import Card
from trash_gain_card import TrashGainEffectCard


class Mine(TrashGainEffectCard):
	coin_gain = 3
	trashable_type_restriction = [Card.CardType.Treasure]
	gainable_type_restriction = [Card.CardType.Treasure]