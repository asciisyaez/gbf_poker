card = {
	"2": 0,
	"3": 1,
	"4": 2,
	"5": 3,
	"6": 4,
	"7": 5,
	"8": 6,
	"9": 7,
	"10": 8,
	"j": 9,
	"q": 10,
	"k": 11,
	"a": 12
}

# Array of ints
# Index corresponds to card enum value
cards = [4] * 13
cards_left = 52

def get_lower(card_index):
	num_cards = 0
	ndx = 0
	while ndx < card_index:
		num_cards += cards[ndx]
		ndx += 1
	return float(float(num_cards) / cards_left) * 100

def get_higher(card_index):
	num_cards = 0
	ndx = card_index + 1
	while ndx < 13:
		num_cards += cards[ndx]
		ndx += 1
	return float(float(num_cards) / cards_left) * 100

plays = 10

while plays > 0:
	found_card = input("Card: ")

	if str(found_card).lower() in card:
		card_index = card[str(found_card).lower()]
	else:
		exit()

	cards[card_index] -= 1
	cards_left -= 1
	print("Higher: %.2f, Lower: %.2f" % (get_higher(card_index), get_lower(card_index)))
	plays -= 1