class CardDeck:
    def __init__(self):
        self.suits = ['Пик', 'Треф', 'Червы', 'Бубен']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
        self.cards = [(value + ' ' + suit) for suit in self.suits for value in self.values]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.cards):
            raise StopIteration
        card = self.cards[self.index]
        self.index += 1
        return card

deck = CardDeck()
for card in deck:
    print(card)
