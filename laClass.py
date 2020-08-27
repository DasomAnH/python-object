class Person:
    alive = True
    species = 'mammal'


​
  def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
​
  def greet(self, other_person):
       if (self.alive):
            print('Hello {}, I am {}!'.format(other_person.name, self.name))
            self.greeting_count += 1
            self.add_friend(other_person)
            other_person.add_friend(self)
        else:
            print(f'{self.name} is lifeless on the floor and says nothing')
​
  def print_contact_info(self):
       print(f"{self.name}'s email: {self.email}")
        print(f"{self.name}'s phone number: {self.phone}")
​
  def add_friend(self, friend):
       self.friends.append(friend)
​
  def num_friends(self):
       return len(self.friends)
​
  def die(self):
       self.alive = False
​
​


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


​
  def print_info(self):
       print(f'{self.year} {self.make} {self.model}')
​
​
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
lachlan = Person("Lachlan", "lachlan@yahoo.com", "678-555-1234")
​
print('-------Friends-------')
​
sonny.greet(jordan)
sonny.greet(lachlan)
sonny.greet(jordan)
jordan.greet(sonny)
jordan.greet(lachlan)
lachlan.greet(sonny)
lachlan.greet(jordan)
​
print(f'Sonny introduced himself {sonny.greeting_count} times')
​
print('------- Contact Info -------')
​
sonny.print_contact_info()
jordan.print_contact_info()
lachlan.print_contact_info()
​
print('-------Friends-------')
​
sonny.add_friend(jordan)
sonny.add_friend(lachlan)
​
print("Sonny's Friends")
for friend in sonny.friends:
    friend.print_contact_info()
​
print("Jordan's Friends")
for friend in jordan.friends:
    friend.print_contact_info()
​
print("Lachlan's Friends")
for friend in lachlan.friends:
    friend.print_contact_info()
​
print('-------')
​
print(f"Sonny has {sonny.num_friends()} friends")
print(f"Jordan has {jordan.num_friends()} friends")
​
print('-------')
​
car = Vehicle('Tesla', 'CyberTruck', 2022)
​
print(car.make, car.model, car.year)
