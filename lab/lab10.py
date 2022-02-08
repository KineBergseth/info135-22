# EXERCISE 1
# Improved Knapsack:
# Create the function detailed_knap_sack() that takes in parameters value, weights and max capacity
# and returns the maximum total profit as well as the weights connected to the items in the sack.


values = [120, 200, 150, 350, 100, 90]
weights = [15, 20, 40, 50, 20, 10]
capacity = 100
n = len(values)


def detailed_knap_sack(values, weights, capacity):
    sack = []
    k = [[0 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]

    for i in range(len(weights) + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                k[i][w] = 0
            elif weights[i - 1] <= w:
                k[i][w] = max(values[i - 1] + k[i - 1][w - weights[i - 1]], k[i - 1][w])
            else:
                k[i][w] = k[i - 1][w]
    # return k[len(weights)][capacity]
    res = k[len(weights)][capacity]
    print(f'Max profit: {res}$')

    w = capacity
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # either the result comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        if res == k[i - 1][w]:
            continue
        else:
            # This item is included.
            sack.append(weights[i - 1])
            # Since this weight is included
            # its value is deducted
            res = res - values[i - 1]
            w = w - weights[i - 1]
    print(f'Weigths used: {sack}')


detailed_knap_sack(values, weights, capacity)


# EXERCISE 2 - OOP classes

class Car:
    def __init__(self, model, year, price, speed=0):
        self.model = model
        self.year = year
        self.price = price
        self.speed = speed

    def start(self):
        print('Vroom vroom')
        self.accelerate(50)

    def brake(self, kmh):
        self.speed -= kmh
        if self.speed <= 0:
            self.speed = 0
            print(f'you slam the breaks. The vehicle is stopped')
        else:
            print(f'you step on the breaks. your current speed is {self.speed} kmh')

    def accelerate(self, kmh):
        self.speed += kmh
        print(f'you step on the gas. your current speed is {self.speed} kmh')

    def get_price(self):
        return self.price


class Student:
    def __init__(self, name, student_id, address, grade=''):
        self.name = name
        self.id = student_id
        self.address = address
        self.grade = grade

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade


''' In Python, getters and setters are not the same as those in other object-oriented programming languages. Basically,
the main purpose of using getters and setters in object-oriented programs is to ensure data encapsulation. Private 
variables in python are not actually hidden fields like in other object oriented languages. 

 If you want private attributes and methods you can implement the class using setters, getters methods 
 otherwise you will implement using the normal way.
 '''


class Flight:
    def __init__(self, origin, destination, airline, number):
        # origin and airline are private attribute in Python
        self._origin = origin
        self.destination = destination
        self._airline = airline
        self.number = number

    # get the value of the private attribute airline
    def get_airline(self):
        return self._airline

    # set the value of airline using an object of a class
    def set_airline(self, airline):
        self._airline = airline

    def get_origin(self):
        return self._origin

    def set_origin(self, origin):
        self._origin = origin


''' @property decorator 
@property is used to get the value of a private attribute without using any getter methods. We 
have to put a line @property in front of the method where we return the private variable. 

To set the value of the private variable, we use @method_name.setter in front of the method. We have to use it as a 
setter. '''


class BankAccount:
    def __init__(self, name, number, balance, acc_type):
        # name and balance are private variables/properties in Python
        self._name = name
        self.number = number
        self._balance = balance
        self.type = acc_type

    # using property decorator, a getter function
    @property
    def name(self):
        return self._name

    # setter function. the attribute and method name must be same which is used to set the value for the attribute
    @name.setter
    def name(self, n):
        self._name = n

    # using property decorator, a getter function
    @property
    def balance(self):
        return self._balance

    # a setter function
    @balance.setter
    def balance(self, n):
        if n < 0:
            print('You cant deposit a negative amount')
        else:
            print(f'You have deposited {n} kr')
            self._balance = n


if __name__ == '__main__':
    print('')
    print('-----CAR-----')
    toyota = Car('T9', 1993, 3000)
    toyota.start()
    toyota.accelerate(10)
    toyota.brake(30)
    toyota.brake(30)

    print('')
    print('-----STUDENT-----')
    sara = Student('sara', 123, 'Furuvegen 1')
    sara.set_grade('A')
    print(sara.get_grade())
    print(sara.grade)
    sara.set_address('granvegen 2')
    print(sara.get_address())

    print('')
    print('-----FLIGHT-----')
    flight1 = Flight('Oslo', 'Riga', 'RyanAir', 'AHG584')
    print(flight1.get_origin())
    flight1.set_origin('Bergen')
    print(flight1.get_origin())
    print(flight1.get_airline())

    print('')
    print('-----BANK ACCOUNT-----')
    customer = BankAccount('steven', 54769832, -3, 'Savings')
    customer.name = 'Ola'
    print(customer.name)
    # customer.balance = -5000
    customer.balance = 3000
    print(customer.balance)
    print('')

'''
FOR MORE INFO ON PRIVATE ATTRIBUTES/METHODS: 
https://www.datacamp.com/community/tutorials/role-underscore-python
FOR MOTE INFO ON GETTERS/SETTERS IN PYTHON: 
https://www.datacamp.com/community/tutorials/property-getters-setters
'''


# EXERCISE 3
# Here we decided to spilt our rocket into three classes. We have one RoEngine class which handles the engine and
# different aspect of that. The comm class has nothing to do with the engine hence its own class. Our RocketMode is a
# class which will initiate different modes of the rocket, and start the different methods of the other classes.
# This way we follow the principles of encapsulation.

# The actual code here is very simple and not the point, the point being the set up of the classes and functions
# Yours probably look different but as long as you follow the principles of OOP that is ok, keep things encapsulated
# An engine should deal with engine things not communication, let the classes be seperate and call each other when needed
# OOP is what is used in most if not all workplaces so try to just get a hang of how a code set up, best way to learn
# to learn this is by doing, much like math. Learning by doing.
class RoEngine:

    def __init__(self):
        self.oil = 35
        self.fuel = 5000
        self.power_level = 0

    def launch(self):
        print("Vroom Vroom")
        self.oil -= 5
        self.fuel -= 50
        self.power_level = 98

    def oil_check(self):
        print("The oil is at", self.oil)

    def fuel_check(self):
        print("The fuel is at", self.fuel)

    def cruise(self, time):
        self.power_level = 50
        self.fuel -= 2 * time
        print("We cruisin on 50% of our power")

    def landing(self):
        i = 10
        while i > -1:
            self.power_level = i
            print("Going in for a landing power level set to ", self.power_level)
            i -= 1


class Communication:

    def __init__(self):
        self.marvin = False

    def send_radio_signal(self, message):
        print("Sending your messeage out in space now", message)

    def call_home(self, nr):
        print("Calling the number, now must work")
        print("RING RING")
        print('They hung up or we did not implement a call function properly')
        self.init_chatbot()

    def init_chatbot(self):
        print("Setting up Marvin for you to talk to instead")
        self.marvin = True


class RocketMode:
    engine = RoEngine()
    comms = Communication()

    def __init__(self):
        self.steering = True
        self.inSpace = False

    def intiate_launch(self):
        print('Start countdown for launch, y/n')
        if input().lower() == 'y':
            i = 10
            while i != 0:
                print(i)
                i -= 1
                if i == 0:
                    self.engine.launch()
                    self.inSpace = True
                    print("lift off")
        else:
            print('Launch aborted')

    def going_cruise(self, time):
        if self.inSpace:
            self.engine.cruise(time)
        else:
            print("cant cruise while on land")

    def landing(self):
        if self.inSpace:
            self.engine.landing()
            self.steering = True
            self.inSpace = False
        else:
            print("cant land while on the ground")

    def call_home(self, nr):
        self.comms.call_home(nr)


# Just to see it run, add the method you like here, not everyone is called here.
class run_it:
    def __init__(self):
        ro = RocketMode()
        ro.intiate_launch()
        ro.engine.fuel_check()
        ro.going_cruise(40)
        ro.call_home(904323)
        ro.landing()


run_it()
