from random import randint

def is_even(number: int) -> bool:
    return number % 2 == 0

def throw_the_dice(amount: int) -> int:
    value = randint(1, 6)
    return 2 * amount if is_even(value) else 0

def play_the_game(initial_amount: int) -> int:
    counter = 0
    profits = initial_amount
    while profits != 0:
        profits -= initial_amount
        profits = profits + throw_the_dice(initial_amount)
        counter += 1
    return counter

if __name__ == "__main__":
    GAME_PLAYED = 100
    BET = 100
    
    game_turns = []
    for i in range(GAME_PLAYED):
        game_turns.append(play_the_game(BET))
    
    print(f"Promedio de turnos en {GAME_PLAYED} juegos: {sum(game_turns) / GAME_PLAYED}")