class Person:
   # Class Attribute

    species = 'mammal'

    # Initiallize / Instance Attributes
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    # Instance Method

    def greet(self, other_person):

        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def contact(self):
        print(f'{self.name}: \n phone:{self.phone} \n Email:{self.email}')


sonny = Person('sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)
jordan.greet(sonny)

sonny.contact()
jordan.contact()
