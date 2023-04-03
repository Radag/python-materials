import random

class Pokemon():
    def __init__(self):
        self.level = 1
        self.maxHealth = 20
        self.health = 20
        self.defenceValue = 1
        self.attackValue = 3
        self.experience = 0

    def attack(self, opponent):
        defended = opponent.defend()
        if(self.attackValue > defended):
            actualAttack = self.getAttackValue(defended)
            opponent.health -= actualAttack
            print(f"{self.name} útočí a {opponent.name} zůstává jenom {opponent.health} životů.")
            self.addExperience(actualAttack)
        else:
            print(f"{opponent.name} se ubránil útoku.")

    def defend(self):
        return self.defenceValue + random.randint(0,2)

    def getAttackValue(self, defended):
        return (self.attackValue + random.randint(0,3)) - defended

    def addExperience(self, experience):
        self.experience = experience
        if self.experience > self.level*3:
            self.level += 1
            self.experience = 0
            self.levelUp()
            print(f"{self.name} zvýšil level na {self.level}")

    def levelUp(self):
        self.health = self.maxHealth

    def fight(self, opponent):
        lastAttacker = self.name
        while(self.health > 0 and opponent.health>0):
            if lastAttacker == self.name:
                opponent.attack(self)
                lastAttacker = opponent.name
            else:
                self.attack(opponent)
                lastAttacker = self.name

        if(self.health > 0):
            print(f"Výtězem je {self.name}")
            return True
        else:
            print(f"Výtězem je {opponent.name}")
            return False



class Bulbasaur(Pokemon):
    name = "Bulbasaur"
    pass

class Charizard(Pokemon):
    name = "Charizard"
    pass

class Pikachu(Pokemon):
    name = "Pikachu"
    pass

class Squirtle(Pokemon):
    name = "Squirtle"
    pass


class Trainer():
    def __init__(self, name):
        self.name = name
        self.pocket = []

    def addPokemon(self, pokemon):
        self.pocket.append(pokemon)

    def fight(self, opponent):
        myVictories = 0
        oponentVictories = 0
        for myPokemon in self.pocket:
            for opponentPokemon in opponent.pocket:
                print(f"Nastupuje {myPokemon.name} proti {opponentPokemon.name}")
                if myPokemon.fight(opponentPokemon):
                    myVictories += 1
                else:
                    oponentVictories += 1

        if myVictories > oponentVictories:
            print(f"Výtězem duelu je {self.name}")
        elif myVictories < oponentVictories:
            print(f"Výtězem duelu je {opponent.name}")
        else:
            print(f"Duel skončil nerozhodně")

bulbasaur = Bulbasaur()
charizard = Charizard()
pikachu = Pikachu()
squirtle = Squirtle()

trainerAsh = Trainer("Ash")
trainerAsh.addPokemon(bulbasaur)
trainerAsh.addPokemon(pikachu)

trainerEthan = Trainer("Ethan")
trainerEthan.addPokemon(charizard)
trainerEthan.addPokemon(squirtle)

trainerAsh.fight(trainerEthan)


