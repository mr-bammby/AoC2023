HIGH_CARD = 0
PAIR = 1
TWO_PAIR = 2
THREE = 3
FULL_HOUSE = 4
FOUR = 5
FIVE = 6
card_list = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
joker_map = [[HIGH_CARD, PAIR, TWO_PAIR, THREE, FULL_HOUSE, FOUR, FIVE],
             [PAIR, THREE, FULL_HOUSE, FOUR, FULL_HOUSE, FIVE, FIVE],
             [THREE, FOUR, FULL_HOUSE, FIVE, FULL_HOUSE, FIVE, FIVE],
             [FOUR, FIVE, FULL_HOUSE, FIVE, FULL_HOUSE, FIVE, FIVE],
             [FIVE, FIVE, FULL_HOUSE, FIVE, FULL_HOUSE, FIVE, FIVE],
             [FIVE, FIVE, FULL_HOUSE, FIVE, FULL_HOUSE, FIVE, FIVE]]

def calc_points_main (cards):
    score = HIGH_CARD
    card_counter = [0] * len(card_list)
    for card in cards:
        card_counter[card_list.index(card)] += 1
    joker_counter = card_counter.pop()
    for num in card_counter:
        if (num == 5):
            score = FIVE
            break
        elif (num == 4):
            score = FOUR
            break
        elif (num == 3):
            if (score == PAIR):
                score = FULL_HOUSE
                break
            else:
                score = THREE
        elif (num == 2):
            if (score == THREE):
                score = FULL_HOUSE
                break
            elif (score == PAIR):
                score = TWO_PAIR
                break
            else:
                score = PAIR
    score = joker_map[joker_counter][score]
    return (score)

def calc_points_additional(cards):
    score = 0
    for card, i in zip(cards, range(len(cards))):
        score += ((len(card_list) + 1) ** (len(cards) - i)) * (len(card_list) - card_list.index(card)) 
    return (score)  

def main(filepath):
    file = open(filepath, "r")
    result = 0
    player_list = []
    sorted_player = []
    i = 0
    for line in file:
        cards, bid = line.split()
        player_list.append([i, cards, int(bid), (calc_points_main(cards) * ((len(card_list) + 1) ** (len(cards) + 1))) + calc_points_additional(cards)])
        i += 1
    sorted_player = sorted(player_list, key=lambda x: x[3])
    place = 1
    for player in sorted_player:
        result += player[2] * place
        place += 1
    print("Result: " + str(result))

if (__name__ == "__main__"):
    main("./07/input1.txt")