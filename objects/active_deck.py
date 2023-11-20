import random

class ActiveDeck:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ActiveDeck, cls).__new__(cls)
            cls._instance.cards = []
            cls._instance.current_index = 0
            cls._instance.deck_name = ""
            cls._instance.active_front_card = ""
            cls._instance.active_back_card = ""
        return cls._instance

    def load_deck(self, deck_data):
        self.cards = [{'front': f, 'back': b} for f, b in zip(deck_data['front'], deck_data['back'])]
        self.current_index = 0
        self.deck_name = deck_data.get('deck_name', '')
        self.update_active_card()

    def update_active_card(self):
        if self.cards:
            self.active_front_card = self.cards[self.current_index]['front']
            self.active_back_card = self.cards[self.current_index]['back']

    def get_current_card(self):
        return {'front': self.active_front_card, 'back': self.active_back_card} if self.cards else {'front': 'No cards', 'back': 'No cards'}

    def next_card(self):
        if self.cards:
            self.current_index = random.randint(0, len(self.cards) - 1)
            self.update_active_card()
        return self.get_current_card()
