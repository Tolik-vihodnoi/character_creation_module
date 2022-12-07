from random import randint

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.__class__.__name__} -{self.BRIEF_DESC_CHAR_CLASS}.'

    def attack(self):
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс урон противнику равный {value_attack}')

    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} урона')

    def special(self):
        return (f'{self.name} применил специальное умение '
                f'{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}»')

class Warrior(Character):
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_SKILL = 'Выносливость'
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')

class Mage(Character):
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_SKILL = 'Атака'
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')

class Healer(Character):
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_SKILL = 'Защита'
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')


def choice_char_class(char_name: str) -> Character:
    """Define hero class."""

    game_classes: dict = {'warrior': Warrior,
                          'mage': Mage,
                          'healer': Healer}

    approve_choice: str = None

    while approve_choice != 'y':
        selected_class: str = input('Введи название персонажа, за которого хочешь '
                                'играть: Воитель — warrior, Маг — mage, '
                                'Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)
        approve_choice: str = input('Нажми (Y), чтобы подтвердить выбор, '
                                    'или любую другую кнопку, чтобы выбрать '
                                    'другого персонажа ').lower()
    return char_class


def start_training(character: Character) -> None:
    """Let user train or skip."""
    comands: dict = {'attack': character.attack,
                     'defence': character.defence,
                     'special': character.special,
                     }

    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd: str = input('Введи команду: ')
        if comands.get(cmd, None):
            action: str = comands[cmd]()
            print(action)
    print('Тренировка окончена.')


if __name__ == '__main__':
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    hero: Character = choice_char_class(char_name)
    start_training(hero)
