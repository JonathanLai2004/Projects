# My method compiles all the analytical functions into a new class "AnalyzePoker"

class AnalyzePoker:
    
    def __init__(self, hand):
        self.cards = hand[:]
        self.card1 = hand[0]
        self.card2 = hand[1]
        self.card3 = hand[2]
        self.card4 = hand[3]
        self.card5 = hand[4]
        self.suits = [(self.cards[i]['suit']) for i in range(5)]
        self.values = [(self.cards[i]['value']) for i in range(5)]
        
    def unique_suits(self):        # iterating through hand, adds suit names from hand to unique_suits_list if not already there
        unique_suits_list = []
        [unique_suits_list.append(self.cards[i]['suit']) for i in range(5) if self.cards[i]['suit'] not in unique_suits_list]
        return unique_suits_list
    
    def unique_values(self):       # iterating through hand, adds values from hand to unique_values_list if not already there
        unique_values_list = []
        [unique_values_list.append(self.cards[i]['value']) for i in range(5) if self.cards[i]['value'] not in unique_values_list]
        return unique_values_list
    
    def frequencies_of_values(self):  # for each value in the hand, adds 1 to the frequency count for that value
        frequency = {}                # in dictionary 'frequency'
        for value in self.values:
            if value in frequency:
                frequency[value] += 1
            else:
                frequency[value] = 1
        return frequency
    
    # Checks for each type of poker hand is below this
    
    def check_four_of_a_kind(self):      # TRUE if one of the values == 4 in dictionary 'frequency' for the hand
        if 4 in list(hand.frequencies_of_values().values()):
            return 1
        return 0
    
    def check_flush(self):               # TRUE if there is only suit in unique_suits_list
        if len(hand.unique_suits()) == 1:
            return 1
        return 0
    
    def check_straight(self):            # TRUE if there are 5 unique values in unique_value_list, and the minimum value is 4 less than max
        if len(hand.unique_values()) == 5:
            if min(hand.values)+4 == max(hand.values):
                return 1
        return 0
    
    def check_three_of_a_kind(self):     # TRUE if one of the values == 3 in dictionary 'frequency' for the hand
        if 3 in list(hand.frequencies_of_values().values()):
                return 1
        return 0            
    
    def check_two_pair(self):            # TRUE if two of the values == 2 in dictionary 'frequency' for the hand
        if list(hand.frequencies_of_values().values()).count(2) == 2:
            return 1
        return 0
        
    def check_one_pair(self):            # TRUE if only one of the values == 2 in dictionary 'frequency' for the hand
        if list(hand.frequencies_of_values().values()).count(2) == 1:
            return 1
        return 0
    
    def check_high_card(self):           # TRUE if all card values are different in the hand
        if len(hand.unique_values()) == 5:
                return 1
        return 0
    
    # Checks for special combination poker hands
    
    def check_royal(self):               # TRUE if hand is both a straight and a flush, and the high value is 13
        if hand.check_straight() == hand.check_flush() == 1:
            if hand.values[4] == 13:
                return 1
        return 0
    
    def check_straight_flush(self):      # TRUE if hand is both a straight and a flush
        if hand.check_straight() == hand.check_flush() == 1:
            return 1
        return 0
    
    def check_full_house(self):          # TRUE if there is both a single pair, and three of a kind
        if hand.check_one_pair() == hand.check_three_of_a_kind() == 1:
                return 1
        return 0
    
    # Because multiple checks may return TRUE for a single hand, the name of the hand will just be the best one
    
    def hand_name(self):
        if hand.check_royal():
            return("Royal Flush")
        elif hand.check_straight_flush():
            return("Straight Flush")
        elif hand.check_four_of_a_kind():
            return("Four of a Kind")
        elif hand.check_full_house():
            return("Full House")
        elif hand.check_flush():
            return("Flush")
        elif hand.check_straight():
            return("Straight")
        elif hand.check_three_of_a_kind():
            return("Three of a Kind")
        elif hand.check_two_pair():
            return("Two Pair")
        elif hand.check_one_pair():
            return("One Pair")
        elif hand.check_high_card():
            return("High Card")

# Using class AnalyzePoker to analyze the probabilities of various hands

# Forming deck
deck = [{'value':i, 'suit':c}
for c in ['spades', 'clubs', 'hearts', 'diamonds']
for i in range(2,15)]

# Making a function to shuffle the deck
import random as rm
def shuffle_deck():
    for i in range(2):
        rm.shuffle(deck)

# for 10000 shuffled hands, it will tally down the name of the best Poker hand category it falls under into experimental_results
experimental_results = []
for i in range(10000):
    shuffle_deck()
    hand = AnalyzePoker(deck[0:5])
    experimental_results.append(hand.hand_name())

# counts how many times each type of poker hand came up and calculates resulting experimental percentage
print("Probability of getting High Card = ", .01 * experimental_results.count('High Card'), "%")
print("Probability of getting One Pair = ", .01 * experimental_results.count('One Pair'), "%")
print("Probability of getting Two Pair = ", .01 * experimental_results.count('Two Pair'), "%")
print("Probability of getting Three of a Kind = ", .01 * experimental_results.count('Three of a Kind'), "%")
print("Probability of getting Straight = ", .01 * experimental_results.count('Straight'), "%")
print("Probability of getting Flush = ", .01 * experimental_results.count('Flush'), "%")
print("Probability of getting Full House = ", .01 * experimental_results.count('Full House'), "%")
print("Probability of getting Four of a Kind = ", .01 * experimental_results.count('Four of a Kind'), "%")
print("Probability of getting Straight Flush = ", .01 * experimental_results.count('Straight Flush'), "%")
print("Probability of getting Royal Flush = ", .01 * experimental_results.count('Royal Flush'), "%")