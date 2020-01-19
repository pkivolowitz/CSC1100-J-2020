import random

def MakeDeck():
    deck = list(range(52))
    random.shuffle(deck)
    return deck

def GetCard(deck):
    if len(deck) > 0:
        return(deck.pop())
    else:
        return -1

def MakeCard(card):
    if card >= 0:
        return { 'rank': card % 13, 'suit': card // 13 }
    else:
        return None

def MakeHand(deck, count):
    hand = []
    for _ in range(count):
        hand.append(MakeCard(GetCard(deck)))
    return hand

def CheckForPairs(hand, precedence, text):
    precedence, text = 0, 'High Card'
    ranks = { }
    for c in hand:
        if c['rank'] in ranks:
            ranks[c['rank']] += 1
        else:
            ranks[c['rank']] = 1

    multiples = sorted(list(ranks.values()), reverse=True)
    if multiples[0] == 2 and multiples[1] == 2:
        precedence, text = 2, 'Two Pair'
    elif multiples[0] == 2:
        precedence, text = 1, 'One Pair'
    elif multiples[0] == 3 and multiples[1] == 2:
        precedence, text = 6, 'Full House'
    elif multiples[0] == 3:
        precedence, text = 3, 'Three of a Kind'
    elif multiples[0] == 4:
        precedence, text = 7, 'Four of a Kind' 
    return precedence, text

def EvaluateHand(hand):
    precedence = 0
    text = ''
    precedence, text = CheckForPairs(hand, precedence, text)
    return precedence, text

if __name__ == "__main__":
    deck = MakeDeck()
    hand = MakeHand(deck, 5)
    precedence, text = EvaluateHand(hand)
    print(precedence, text)