# Define variables
from pip._vendor.distlib.compat import raw_input

number_one = 1
age_of_grandma = 79


# Define some functions

def print_hello():
    print('Hello')


def times_four(input):
    print(input * 4)


# Define a class

class BaseballCard:
    def __init__(self):
        self.brand = raw_input('What brand is the card?')
        self.player = raw_input('What player is on the card?')
        self.price = raw_input('How much did it cost?')
        self.age = raw_input('How old is it (in years)?')

    def printdetails(self):
        print('This card of ' + self.player + " " + self.brand, "card, of " + self.player, "is " + self.age +
              "years old and costs" + self.price + " dollars")
