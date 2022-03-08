from random import choice

FILE_SECRET_WORDS = ''
FILE_DICTIONARY = ''


def get_secret_words():
    """
    :return: Gets list of secret words that can be picked
    """
    words = []
    return words


def get_dictionary():
    """
    :return: Gets list of secret words that can be picked
    """
    words = []
    return words


def pr_green(letter):
    return f'{letter}'


def pr_orange(letter):
    return f'{letter}'


def pr_red(letter):
    return f'{letter}'


def pr_overline(letter):
    return f'{letter}'


class Wordle:
    def __init__(self):
        self.wins = 0
        self.losses = 0

    def select_word(self):
        pass

    def validate_guess(self):
        pass

    def give_feedback(self):
        pass

    def print_stats(self):
        pass

    def play(self):
        print('WORDLE')
        self.select_word()
        guess = input(f'Insert 5-letter guess:')
        while len(guess) != 5:
            print(f'Not valid input. Insert 5-letter word')
            guess = input(f'Insert 5-letter guess:')
        print(guess)
        again = input(f'play again? y/n')
        if again == 'y':
            self.play()
        else:
            print(f'good game. here is your stats:')
            self.print_stats()


w = Wordle()
w.play()
