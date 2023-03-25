from map import Map
from states_data import StatesData


class Game:
    def __init__(self):
        self.map = Map()
        self.data = StatesData()

    def play(self):
        game_over = False
        while not game_over:
            guess = self.map.get_guess()
            coordinates = self.data.check_guess(guess)
            print(coordinates)
            if coordinates:
                self.map.reveal_state(coordinate=coordinates[0][1:], name=coordinates[0][0])
            if guess == "Exit" or self.map.is_game_over():
                game_over = True
        self.map.set_exit()
