from random import randint


def attack(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'\n\n{char_name} нанёс урон'
                f'противнику равный {5 + randint(3, 5)}\n')
    if char_class == 'mage':
        return (f'\n\n{char_name} нанёс урон'
                f'противнику равный {5 + randint(5, 10)}\n')
    if char_class == 'healer':
        return (f'\n\n{char_name} нанёс урон'
                f'противнику равный {5 + randint(-3, -1)}\n')


def defence(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')


def special(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'\n\n{char_name} применил специальное'
                f'умение «Выносливость {80 + 25}»\n')
    if char_class == 'mage':
        return (f'\n\n{char_name} применил специальное'
                f'умение «Атака {5 + 40}»\n')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение «Защита {10 + 30}»')


def start_training(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('\n\n\n\n Введи одну из команд: attack — чтобы'
          'атаковать противника, defence — чтобы блокировать\n'
          'атаку противника или special — чтобы\n'
          'использовать свою суперсилу.\n')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd: str = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('\n\n\nВведи название персонажа,'
                           ' за которого хочешь играть: Воитель — warrior,\n'
                           'Маг — mage, Лекарь — healer: \n')
        if char_class == 'warrior':
            print('\n\nВоитель — дерзкий воин ближнего'
                  'боя. Сильный, выносливый и отважный.\n')
        if char_class == 'mage':
            print('\n\nМаг — находчивый воин'
                  'дальнего боя. Обладает высоким интеллектом.\n')
        if char_class == 'healer':
            print('\n\nЛекарь — могущественный заклинатель.'
                  'Черпает силы из природы, веры и духов.\n')
        approve_choice = input('\n\n\nНажми (Y), чтобы подтвердить выбор,'
                               ' или любую другую кнопку,\n'
                               'чтобы выбрать другого персонажа \n').lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))


main()