from abc import ABC, abstractmethod
import random


# random event where an animal gets sick, and it might or might not recover
def decease():
    # Choose random animal to make sick
    random_no = random.randint(0, len(Animal.all_animals) - 1)
    # create random survival chance
    survival_chance = random.randint(0, 100)
    print(
        f'{Animal.all_animals[random_no].name} has fallen ill, and might die. Their chance at survival is '
        f'{survival_chance} %')

    # if survival change is 50 or grater, animal survives. else it dies.
    if survival_chance >= 50:
        print(f'{Animal.all_animals[random_no].name} has improved greatly, and is now well again')
    if survival_chance < 50:
        Animal.all_animals[random_no].alive = False
        print(f'{Animal.all_animals[random_no].name} was too sick to recover, and has now died')

    # * this is not perfect:  animal is not removed from enclosure, and they might already be dead before they get ill.


class Animal(ABC):
    all_animals = []

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.alive = True
        Animal.all_animals.append(self)

    def __repr__(self):
        return f'{self.name} the {self.species}'

    def __str__(self):
        return f'{self.name} the {self.species}, Alive: {self.alive}'

    @abstractmethod
    def speak(self):
        pass


class Mammal(Animal):
    skin_type = 'hair'
    speech_action = 'grunts in your direction'

    def __init__(self, name, species, is_meat_eater):  # Pass parent variables to super.
        super().__init__(name, species)
        self.carnivorous = is_meat_eater  # bool, does mammal eat meat or not carnivorous /herbivore

    def speak(self):
        return f'{self.name} {Mammal.speech_action}'

    def __str__(self):
        return super().__str__() + f' Skin: {Mammal.skin_type}, Carnivorous: {self.carnivorous} '


class Reptile(Animal):
    skin_type = 'scales'
    speech_action = 'hisses at you with hateful eyes'

    def __init__(self, name, species, is_venomous, is_meat_eater):
        super().__init__(name, species)  # Pass parent variables to super.
        self.venomous = is_venomous  # bool, does reptile have venomous bite
        self.carnivorous = is_meat_eater  # bool, does mammal eat meat or not. carnivorous/herbivore

    def speak(self):
        return f'{self.name} {Reptile.speech_action}'

    def __str__(self):
        return f'{self.name} the {self.species}: Skin: {Reptile.skin_type}, Alive: {self.alive}, ' \
               f'Carnivorous: {self.carnivorous}, Venemous: {self.venomous} '


class Bird(Animal):
    skin_type = 'feathers'
    speech_action = 'squawks in anger to claim its territory'

    def __init__(self, name, species, can_fly):
        super().__init__(name, species)  # Pass parent variables to super.
        self.can_fly = can_fly  # bool, can the bird fly or not
        self.carnivorous = False  # all birds are herbivores

    def speak(self):
        return f'{self.name} {Bird.speech_action}'

    def __str__(self):
        return f'{self.name} the {self.species}: Skin: {Bird.skin_type}, Alive: {self.alive}, ' \
               f'Carnivorous: {self.carnivorous}, Can fly: {self.can_fly} '


class Enclosure:
    def __init__(self, enclosure_id):
        self.id = enclosure_id
        self.animals = set()  # utilize set to store animals, lists are also good

    def add_animal(self, animal):
        self.is_conflict(animal) # chech if animal is compatible with existing
        self.check_if_prey()  # if advice ignored, check if someone dies :o

    def remove_animal(self, animal):
        self.animals.remove(animal)
        
    def is_conflict(self, new_animal):
        for animal in self.animals:
            if animal.carnivorous != new_animal.carnivorous:
                print(f'''
                you are trying to put {new_animal.name} in enclosure {self.id}. Are you sure you want to have a carnivorous and herbivore in the same cage?
                ''')
                answer= input('do you want to proceed anyway (y/n)?')
                if answer == 'n':
                    print(f'you have chosen to not put {new_animal.name} in the cage. you have avoided conflict', end='\n\n')
                    return
        else: 
            self.animals.add(new_animal)
            print(f'added {new_animal.name} to enclosure {self.id}', end='\n\n')

    def check_if_prey(self):
        # when any new animal enters enclosure check if any animals in cage should be eaten
        death_log = {}  # keep track of dead animals and death message
        killing_rampage = False

        # if one of the animals are carnivore, they go on killing rampage
        for animal in self.animals:
            if animal.carnivorous:
                killing_rampage = True

        # If there are herbivores, they are killed
        if killing_rampage:
            for animal in self.animals:
                if not animal.carnivorous:
                    animal.alive = False
                    death_log[animal] = f'{animal.name} the {animal.species} got eaten. may he rest in piece'

        if len(death_log) > 0:  # are there any deaths to be announced?
            print('Oh no! You accidentally placed a carnivore with herbivore(s). Thats not promising')
            # print all dead animals
            for animal in death_log:
                print(death_log[animal])
                self.remove_animal(animal)

    def __str__(self):
        # print enclosure id, number of animals, and all animals in it
        return f'{self.__class__.__name__} {self.id} has {len(self)} animals: {self.animals}'

    def __len__(self):
        return len(self.animals)


class Zoo:
    def __init__(self, name):
        self.no_animals = 0
        self.name = name
        self.enclosures = []

    # go through all enclosures, and count animals
    def count_animals(self):
        self.no_animals = 0
        for animal in self.enclosures:
            self.no_animals += len(animal.animals)
        return self.no_animals

    def no_of_enclosures(self):
        return len(self.enclosures)

    # add an existing enclosure to zoo register
    def add_enclosure(self, enclosure_id):
        if type(enclosure_id) == Enclosure:
            self.enclosures.append(enclosure_id)
        else:
            print(f'Failed to add enclosure to zoo register. The item you are trying to add in not an enclosure. It is '
                  f'a {enclosure_id.__class__.__name__} duhh')

    def __str__(self):
        message = f'''
            {self.name} is a diverse zoo, with many interesting animals:
            We have a total of {self.count_animals()} animals living in {self.no_of_enclosures()} different enclosures
                '''
        return message

    # print enclosure facts
    def enclosure_facts(self):
        for enclosure in self.enclosures:
            print(enclosure)

    # print animal facts
    @staticmethod
    def animal_facts():
        for animal in Animal.all_animals:
            print(animal)

    @staticmethod
    def welcome_message():
        return f'Welcome to my zoo! Here we have many fun animals to display'


if __name__ == '__main__':
    zoo = Zoo('Zoolandia')
    print(zoo.welcome_message())
    print('')

    # create animals
    mammal1 = Mammal('Ferela', 'lion', True)
    mammal2 = Mammal('Leatboon', 'lemur', False)
    mammal3 = Mammal('Doonok', 'donkey', False)
    mammal4 = Mammal('Lurtacar', 'lemur', False)
    reptile1 = Reptile('Fereetteoci', 'frog', False, False)
    reptile2 = Reptile('Snakossum', 'snake', True, True)
    reptile3 = Reptile('Citigator', 'crocodile', False, True)
    bird1 = Bird('Flautingo', 'flamingo', True)
    bird2 = Bird('Malliceo', 'parrot', True)
    bird3 = Bird('Tucoda', 'penguin', False)
    print(mammal1)

    # create enclosures and add animals
    enclosure1 = Enclosure('1')
    enclosure1.add_animal(mammal2)
    enclosure1.add_animal(mammal3)
    enclosure1.add_animal(mammal4)
    enclosure2 = Enclosure('2')
    enclosure2.add_animal(bird3)
    enclosure2.add_animal(mammal1)
    enclosure2.add_animal(reptile3)
    enclosure3 = Enclosure('3')
    enclosure3.add_animal(reptile1)
    enclosure3.add_animal(reptile2)
    enclosure4 = Enclosure('4')
    enclosure4.add_animal(bird1)
    enclosure4.add_animal(bird2)

    # add enclosures to zoo
    zoo.add_enclosure(enclosure1)
    zoo.add_enclosure(enclosure2)
    zoo.add_enclosure(enclosure3)
    zoo.add_enclosure(enclosure4)
    # these should produce error message in console, they are not enclosures!
    zoo.add_enclosure(bird1)
    zoo.add_enclosure(zoo)

    print(zoo)
    print(mammal3.speak())
    print(reptile2.speak())
    print(bird1.speak())

    print('')
    zoo.enclosure_facts()
    print('')
    zoo.animal_facts()

    print('')
    print(f'Is bird 3 alive: {bird3.alive}')  # he should be dead
    print('')
    print('RANDOM EVENT')
    decease()
