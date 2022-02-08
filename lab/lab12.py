"""
Exercise math in python?

Create a functions that calculate this function f(x)=4π(√(3/x)+x^6)
and then a method that test if it is correct and it only runs the function for f(2) if it knows the function is correct
"""
import math


def func_solver(x):
    # math.sqrt does not like negative numbers and will throw an ValueError. We can use assert to validate input
    #assert x >= 0, 'only positive numbers'
    solution = 4 * math.pi * (math.sqrt(3 / x) + math.pow(x, 6))  # Change something here to see error
    return solution


def test_func():
    assert func_solver(3) == 9173.450548482197, "Should be 9173 and some decimals, somethings off"
    assert func_solver(1) == 34.33196298516978, "Should be 34 and some decis, somethings off"


# if nothing happens then it is correct. if it crashes and post the error message then the calculations are wrong
try:
    test_func()
except AssertionError as tex:
    print(tex)
else:
    mat = func_solver(2)
    print("As we know the function is correct the answer for when x is 2 is: ", mat)


# Battleship!

"""
Battleships

There are no "correct" answers but the answer should contain at least a "map class", a boat class where the different
type of boats inherit from that class, a game class which keeps track of the game as it goes along, a player class
and a bot class. Other classes would probably also be implemented but that varies on how advanced one would make the game
Bonus points if  info on what variables and how to actually create this (more detailed). As this
was a excercise in inf101 which is semi equivalent to this course it is expected given enough you would manage to solve
this.
"""

class Ship(object):
    """Type of ship"""

    # declare ship length
    # declare ship name/type
    # declare ship position/coordinates: column, row
    # keep track of hits
    # coordinates

    def is_sunk(self):
        """ Is this ship sunk or not? """

    def place(self, col, row, direction):
        """Place ship.

        Given a column, row, and direction a ship will occupy, set coordinates property.
        Raise exception if direction/coords are illegal (not valid inputs)

        This is meant to be an abstract class--you should subclass it
        for individual ship types."""


# The ships are all subclasses of the Ship class
class AircraftCarrier(Ship):
    # declare ship length
    # declare ship name/type
    pass


class Destroyer(Ship):
    # declare ship length
    # declare ship name/type
    pass


class Submarine(Ship):
    # declare ship length
    # declare ship name/type
    pass


class Battleship(Ship):
    # declare ship length
    # declare ship name/type
    pass


class Player(object):
    """Object for a player.

    The Player class represents an individual player. It holds information about
    their name, board, and ships. It also has a link to the other player ("opponent"),
    which makes it easy to find the other player.
    """

    def __init__(self, name):
        """Create player:

        - set up their board
        - set up their (empty initially) list of ships"""

    def place_ship(self, ship, col, row, direction):
        """Place a ship on the board at col, row, going in a direction.

        :col: 0-based column
        :row: 0-based row
        :direction: Horizontal og vertical """

    def place_ships(self):
        """Prompt a player to place their ships."""

    def show_board(self):
        """Print out board:
        indicate misses, hits, destroyed ships and nothing there on each coordinate point """

    def handle_shot(self, col, row):
        """Handle being shot at at col, row.

        If the shot is in an already-tried spot:
        - raise ValueError("You've already played there")

        update board to show if it was a miss, hit a ship or if a ship got destroyed"""

    def is_dead(self):
        """Is player dead (out of ships)?"""


class Game(object):
    """Battleship game
    The Game class represents a game and holds the state of the game (player1, player2, and the current player) """

    # keep track of player objects

    def __init__(self, player1_name, player2_name):
        """Create game.

        Create players, assign each other as opponents.
        """

    def setup_ships(self):
        """Prompt both players to place their ships."""

    def play(self):
        """Main game loop.

        Keep playing until a player has lost all their ships.

        - show the player their private board
        - show the player their opponent's non-secret board
        - prompt for a move
        - the opponent handles the player's move
        """


def play(player1_name, player2_name):
    """PLay battleship!

    create a game, prompts the players for setup (placing the ships), and shows the instructions.
    It then enters the main game loop.
    """

