import random

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
card_names = ['Ace', 'Duece', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

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

def CheckForStraights(hand, precedence, text):
    r = []
    p, t = 0, ''
    for c in hand:
        r.append(c['rank'])
    r = sorted(r)
    has_ace = r[0] == 0
    is_straight_over_four_cards = True
    for i in range(2, 5):
        if r[i] != r[i-1] + 1:
            is_straight_over_four_cards = False
            break
    if not is_straight_over_four_cards:
        return precedence, text
    high_card = card_names[r[4]]
    if is_straight_over_four_cards and r[0] + 1 == r[1]:
        # is a natual straight
        p, t = 4, 'Straight with '
    elif is_straight_over_four_cards and has_ace and r[4] == 12:
        p, t = 4, 'Straight with '
        high_card = 'Ace'
    if p > precedence:    
        precedence, text = p, t + high_card + ' High'
    if precedence == 5:
        #breakpoint()
        if high_card == 'Ace':
            precedence, text = 9, 'Royal Straight ' + text
        else:
            precedence, text = 8, 'Straight ' + text + ' with ' + high_card + ' High'
    return precedence, text

def CheckForFlushes(hand, precedence, text):
    s = { }
    p, t = 0, ''
    for c in hand:
        if c['suit'] in s:
            s[c['suit']] += 1
        else:
            s[c['suit']] = 1
    multiples = sorted(list(s.values()), reverse=True)
    if multiples[0] == 5:
        p, t = 5, 'Flush in ' + suits[hand[0]['suit']]
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
    precedence, text = CheckForStraights(hand, precedence, text)
    return precedence, text

if __name__ == "__main__":
    deck = MakeDeck()
    hand = MakeHand(deck, 5)
    hand = [{'rank': 0, 'suit': 0}, {'rank': 9, 'suit': 0}, {'rank': 10, 'suit': 0}, {'rank': 11, 'suit': 0}, {'rank': 7, 'suit': 1}]
    precedence, text = EvaluateHand(hand)
    print(precedence, text)

def test_high_card():
    deck = MakeDeck()
    hand = MakeHand(deck, 5)
    hand = [{'rank': 0, 'suit': 0}, {'rank': 9, 'suit': 0}, {'rank': 10, 'suit': 0}, {'rank': 11, 'suit': 0}, {'rank': 7, 'suit': 1}]
    precedence, text = EvaluateHand(hand)
    assert(text == 'High Card' and precedence == 0)

def test_straight_flush():
    deck = MakeDeck()
    hand = MakeHand(deck, 5)
    hand = [{'rank': 0, 'suit': 0}, {'rank': 9, 'suit': 0}, {'rank': 10, 'suit': 0}, {'rank': 11, 'suit': 0}, {'rank': 8, 'suit': 0}]
    precedence, text = EvaluateHand(hand)
    assert(text == 'Straight Flush in Clubs with Queen High' and precedence == 8)

def test_royal_straight_flush():
    deck = MakeDeck()
    hand = MakeHand(deck, 5)
    hand = [{'rank': 0, 'suit': 1}, {'rank': 9, 'suit': 1}, {'rank': 10, 'suit': 1}, {'rank': 11, 'suit': 1}, {'rank': 12, 'suit': 1}]
    precedence, text = EvaluateHand(hand)
    assert(text == 'Royal Straight Flush in Diamonds' and precedence == 9)

def test_one_pair():
    deck = MakeDeck()
    hand = MakeHand(deck, 5)
    hand = [{'rank': 0, 'suit': 1}, {'rank': 9, 'suit': 1}, {'rank': 0, 'suit': 2}, {'rank': 11, 'suit': 1}, {'rank': 12, 'suit': 1}]
    precedence, text = EvaluateHand(hand)
    assert(text == 'One Pair' and precedence == 1)

def test_two_pair():
    deck = MakeDeck()
    hand = MakeHand(deck, 5)
    hand = [{'rank': 0, 'suit': 1}, {'rank': 9, 'suit': 1}, {'rank': 0, 'suit': 2}, {'rank': 9, 'suit': 3}, {'rank': 12, 'suit': 1}]
    precedence, text = EvaluateHand(hand)
    assert(text == 'Two Pair' and precedence == 2)

def test_three_of_a_kind():
    deck = MakeDeck()
    hand = MakeHand(deck, 5)
    hand = [{'rank': 0, 'suit': 1}, {'rank': 9, 'suit': 1}, {'rank': 0, 'suit': 2}, {'rank': 0, 'suit': 3}, {'rank': 12, 'suit': 1}]
    precedence, text = EvaluateHand(hand)
    assert(text == 'Three of a Kind' and precedence == 3)