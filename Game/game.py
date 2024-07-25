from abc import ABC, abstractmethod
import random
import pickle


class Character(ABC):
    def __init__(self, name):
        self.name = name
        self._exp = 0
        self._level = 1
        self._base_health = 100
        self._current_health = self._base_health
        self._critical_hit = 0
        self._critical_damage = 0
        self.inventory = Inventory()
        self._equipped_cloth = EquippedItems()

    @property
    def attack(self):
        attack = int(self.default_attack) + self._equipped_cloth.attack_boost
        return attack

    @property
    def defence(self):
        defence = int(self.default_defence) + self._equipped_cloth.defence_boost
        return defence

    @property
    def health(self):
        health = int(self._base_health) + self._equipped_cloth.health_boost
        return health

    @property
    def level(self):
        return self._level

    @property
    def base_health(self):
        return not self._base_health

    @base_health.setter
    def base_health(self, value):
        self._base_health = value

    @abstractmethod
    def default_attack(self):
        pass

    @abstractmethod
    def default_defence(self):
        pass

    def equip(self, item):
        result = self._equipped_cloth.equip_item(item)
        return result

    def unequip(self, slot):
        result = self._equipped_cloth.unequip_item(slot)
        return result

    def gain_exp(self, amount):
        self._exp += amount
        if self. _exp >= self._level * 100:
            self._exp -= self._level * 100
            self._level += 1
            self._base_health += 20
            self._current_health = self._base_health

    def __repr__(self):
        return (f'Ваше Ник - {self.name} \nВаши статы: \n'
                f'Атака - {self.attack} \n'
                f'Защита - {self.defence} \n'
                f'Опыт - {self._exp} \n'
                f'Левел - {self._level} \n'
                f'Здоровье - {self.health} \n'
                f'Критический удар - {self._critical_hit} \n'
                f'Критический урон - {self._critical_damage} \n'
                f'Инвентарь - {self.inventory} \n'
                f'{self._equipped_cloth}')

    def __str__(self):
        return self.__repr__()


class Warrior(Character):
    default_attack = 50
    default_defence = 20


class Mage(Character):
    default_attack = 40
    default_defence = 25


class Rogue(Character):
    default_attack = 35
    default_defence = 30


class Paladin(Character):
    default_attack = 30
    default_defence = 35


class Item:
    def __init__(self, name, attack_boost=0, defence_boost=0, health_boost=0, slot=None):
        self.name = name
        self.attack_boost = attack_boost
        self.defence_boost = defence_boost
        self.health_boost = health_boost
        self.slot = slot

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        return False

    def __repr__(self):
        return ', '.join(str(item.name) for item in self.items)

    def __str__(self):
        return self.__repr__()


class EquippedItems:
    def __init__(self):
        self.items = {
            'helmet': None,
            'left_hand': None,
            'right_hand': None,
            'shoes': None,
            'ring': None
        }

    @property
    def attack_boost(self):
        return sum(item.attack_boost for item in self.items.values() if isinstance(item, Item))

    @property
    def defence_boost(self):
        return sum(item.defence_boost for item in self.items.values() if isinstance(item, Item))

    @property
    def health_boost(self):
        return sum(item.health_boost for item in self.items.values() if isinstance(item, Item))

    def equip_item(self, item):
        if item.slot in self.items:
            if self.items[item.slot] is None:
                self.items[item.slot] = item
                return item.slot

    def unequip_item(self, slot):
        if slot in self.items:
            if self.items[slot] is not None:
                item = self.items[slot]
                self.items[slot] = None
                return item

    def __repr__(self):
        equipped_items = {slot: (item if item else 'Пусто') for slot, item in self.items.items()}
        return f'Одетая одежда - {equipped_items}'

    def __str__(self):
        return self.__repr__()


class Bot(Character):
    def __init__(self, name, level):
        super().__init__(name)
        self._level = level
        self._base_health = 50 + (level * 10)
        self._current_health = self._base_health

    @property
    def default_attack(self):
        return 20 + (self._level * 5)

    @property
    def default_defence(self):
        return 10 + (self._level * 5)


class Game:
    def __init__(self):
        self.players = []
        self.bots = []

    def add_player(self, player):
        self.players.append(player)

    def add_bot(self, bot):
        self.bots.append(bot)

    def battle(self, player1, player2):
        print(f'Бой между {player1.name} и {player2.name} начинается!')
        while player1.health > 0 and player2.health > 0:
            self._hit(player1, player2)
            if player2.health > 0:
                self._hit(player2, player1)
        if player1.health > 0:
            winner = player1
            loser = player2
        else:
            winner = player2
            loser = player1
        exp_gain = abs(winner.level - loser.level) * 10
        winner.gain_exp(exp_gain)
        print(f'{winner.name} получил {exp_gain} опыта')
        return f'Выиграл - {winner.name}, проиграл - {loser.name}'

    @staticmethod
    def _hit(attacker, defender):
        damage = attacker.attack - defender.defence
        if isinstance(attacker, Warrior) and isinstance(defender, Mage):
            damage *= 1.15
        elif isinstance(attacker, Mage) and isinstance(defender, Rogue):
            damage *= 1.15
        elif isinstance(attacker, Rogue) and isinstance(defender, Paladin):
            damage *= 1.15
        elif isinstance(attacker, Paladin) and isinstance(defender, Warrior):
            damage *= 1.15
        damage = max(damage, 0)
        defender.base_health -= damage

    def forest_battle(self, player):
        while True:
            print('Вы в лесу')
            bot_level = random.randint(player.level - 1, player.level + 1)
            bot = Bot(f'Бот {bot_level}', bot_level)
            print(self.battle(player, bot))
            player_input = input('Продолжить игру, да или нет?')
            if player_input != 'да':
                break

    def save_game(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f'Игра сохранена - {filename}')

    @staticmethod
    def load_game(filename):
        with open(filename, 'rb') as file:
            load_game = pickle.load(file)
        return load_game


warrior = Warrior('Conan')
varvar = Warrior('Varvar')
helmet = Item('Шлем', 10, 30, 20, 'helmet')
sward = Item('Меч', 30, 10, 10, 'right_hand')
varvar.inventory.add_item(helmet)
varvar.inventory.add_item(sward)
varvar.equip(helmet)
varvar.equip(sward)
game = Game()
game.add_player(warrior)
game.add_player(varvar)
print(game.battle(warrior, varvar))
game.forest_battle(varvar)
sward_left = Item('Меч', 100, 10, 10, 'left_hand')
varvar.equip(sward_left)
game.save_game('Game/saved_game1')
loaded_game = Game.load_game('Game/saved_game1')
loaded_game.forest_battle(varvar)
