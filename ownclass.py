class Vehicle:

    # Initiallize / Instance Attributes
    def __init__(self, year, make, model):
        self.make = make
        self.model = model
        self.year = year

    # Instance Method
    def print_info(self, car):
        print('{},{},{}'.format(self.year, self.make, self.model))


class Person:
    # Intiiallize / Instance Attributes
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.friend_counter = 0
        self.greeting_count = 0

    # Instance Method

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        self.add_friend(other_person)

    def print_contct(self):
        print(f'{self.name}\'s Email:{self.email} \n{self.name}\'s phone:{self.phone}')

    def add_friends(self, friend):
        self.friends.append(friend)
        self.friend_counter += 1

    def num_friends(self):
        # return self.friend_counter
        return len(self.friends)


car = Vehicle('2022', 'Tesla', 'CyberTruck')

sonny = Person('sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('jordan', 'jordan@aol.com', '495-586-3456')
dasom = Person('dasom', 'dasom@gmail.com', '404-892-1234')

car.print_info(car)
print("-----------------")
Person.print_contct(sonny)
jordan.add_friends(sonny)

print(f"sonny has {sonny.num_friends()}friends")
print("-----------------")

sonny.greet(jordan)
jordan.greet(dasom)
