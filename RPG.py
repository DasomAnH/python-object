class Hero:

    species = 'Alien'

    def __init__(self, name, power, health, attack):
        self.name = name
        self.power = power
        self.health = health
        self.attack = attack

    def Hero_content(self):
        print(
            f'Hero \'{self.name}\' has power {self.power} and health {self.health}.')

    def enemy(self):
        self.attack(goblin)


class Goblin:

    species = 'goblin'

    def __init__(self, name, power, health, attack):
        self.name = name
        self.power = power
        self.health = health
        self.attack = attack

    def Goblin_content(self):
        print(
            f'Goblin \'{self.name}\' has power {self.power} and health {self.health}')

    def enemy(self):
        self.attack(hero)


hero = Hero('ironman', 10, 5, 'goblin')
goblin = Goblin('enemy', 6, 2, 'hero')

print('---start---')
hero.Hero_content()
goblin.Goblin_content()


print('---stage1 ---')

user_input = print(
    str(input('you are the hero, Do you want starting game?(y/n)')))


def main():

    while goblin.alive() and hero.alive():
        print("You have %d health and %d power." % (hero.health, hero.power))
        print("The goblin has %d health and %d power." %
              (goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":

            goblin.health -= hero.power
            print("You do %d damage to the goblin." % hero.power)
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            hero.health -= goblin.power
            print("The goblin does %d damage to you." % goblin.power)
            if hero.health <= 0:
                print("You are dead.")


main()
