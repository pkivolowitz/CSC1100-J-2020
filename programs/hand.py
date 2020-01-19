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

def CheckForFlushes(hand, precedence, text):
    suits = { }
    p, t = 0, ''
    for c in hand:
        if c['suit'] in suits:
            suits[c['suit']] += 1
        else:
            suits[c['suit']] = 1
    multiples = sorted(list(suits.values()), reverse=True)
    if multiples[0] == 5:
        p, t = 5, 'Flush'
    if p > precedence:    
        precedence, text = p, t
    return precedence, text


def CheckForPairs(hand, precedence, text):
    ranks = { }
    p, t = 0, ''
    for c in hand:
        if c['rank'] in ranks:
            ranks[c['rank']] += 1
        else:
            ranks[c['rank']] = 1

    multiples = sorted(list(ranks.values()), reverse=True)
    if multiples[0] == 2 and multiples[1] == 2:
        p, t = 2, 'Two Pair'
    elif multiples[0] == 2:
        p, t = 1, 'One Pair'
    elif multiples[0] == 3 and multiples[1] == 2:
        p, t = 6, 'Full House'
    elif multiples[0] == 3:
        p, t = 3, 'Three of a Kind'
    elif multiples[0] == 4:
        p, t = 7, 'Four of a Kind'
    if p > precedence:
        precedence, text = p, t
    return precedence, text

def EvaluateHand(hand):
    precedence, text = 0, 'High Card'
    precedence, text = CheckForPairs(hand, precedence, text)
    precedence, text = CheckForFlushes(hand, precedence, text)

    return precedence, text

if __name__ == "__main__":
    deck = MakeDeck()
    hand = MakeHand(deck, 5)
    precedence, text = EvaluateHand(hand)
    print(precedence, text)