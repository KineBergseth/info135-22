import random
import Stack


class Aces:
    values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
              "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    suits = ("♠", "♥", "♣", "♦")

    def __init__(self):
        self.deck = self.create_shuffed_deck()
        self.stacks = self.deal_cards()  # Exercise 3.a) write this method
        self.set_possible()

    # 3.a ) #STUB
    def deal_cards(self):
        """Return a list of 4 Stacks, each stack contains 13 cards (Cards are in self.deck)"""
        # [Code for 3.a)]
        # test buy inspecting self.stacks
        output = []
        instance_names = ['s0', 's1', 's2', 's3']
        for idx, name in enumerate(instance_names):
            name = Stack.Stack()
            for x in self.deck[idx::4]:  # ::4 takes every 4-th element of deck - step parameter with index as start
                name.push(x)
            output.append(name)
        return output

        """
        stacks = [Stack.Stack(), Stack.Stack(), Stack.Stack(), Stack.Stack()]
        for card in range(0, len(self.deck), 4):
            stacks[0].push(self.deck[card])
            stacks[1].push(self.deck[card + 1])
            stacks[2].push(self.deck[card + 2])
            stacks[3].push(self.deck[card + 3])
        return stacks
        """

    # 3.b) #STUB
    def peek_piles(self):
        """return list of the top four cards (list of tuples)"""
        # [Code for 3.b)]
        # Return example [('♠', 'J'), ('♠', '3'), ('♠', 'K'), ('♦', 'Q')]
        top_cards = []
        for x in self.stacks:
            top_cards.append(tuple(x.peek()))
        return top_cards

    # 3.c) #STUB
    def remove_card(self, stack_index):
        """pop card from a stack based on given index (self.stacks[stack_index]),
        if stack is empty notice the user (see Stack.pop())"""
        # [Code for 3.c)]
        selected_stack = self.stacks[stack_index]
        if selected_stack.isEmpty():
            print("oh my, is appears that the stack is empty!")
        else:
            selected_stack.pop()

    def create_shuffed_deck(self):
        """Creates a shuffled deck of 52 cards"""
        deck = [(suit, value) for suit in self.suits for value in self.values.keys()]
        random.shuffle(deck)
        return deck

    def choose_card(self):
        """Choose a card to remove, if card is valid card is removed from stack"""
        self.display_top_cards()
        cards = self.peek_piles()
        # added Try Except to make sure game does not break when typing wrong input, and allow user to type input again
        while True:
            try:
                choice = int(input("Choose a card (0-3):\n>"))
                if choice > 3:
                    raise ValueError  # this will send it to the print message and back to the input option
                break
            except ValueError:
                print("That's not an option! Input must be 0, 1, 2 or 3")
        chosen = cards[choice]
        for card in cards:
            if card[0] == chosen[0] and self.values[card[1]] > self.values[chosen[1]]:
                self.remove_card(choice)
                return
        print("Invalid choice")

    def set_possible(self):
        "Check for if it is possible to continue"
        self.possible = set(self.suits) != set([c[0] for c in self.peek_piles()])

    def play(self):
        """START GAME"""
        while not self.possible:
            self.deck = self.create_shuffed_deck()
            self.set_possible()
        while self.possible:
            self.choose_card()
            self.set_possible()
        self.display_top_cards()
        print("no Action Possible, you lost :(")

    def display_top_cards(self):
        "Display the top four cards for the user"
        cards = self.peek_piles()
        final_str = "0 \t\t1 \t\t2 \t\t3\n"
        for card in cards:
            final_str += card[0] + card[1] + "\t\t"
        print(final_str)


game = Aces()
game.play()
