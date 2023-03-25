import pandas


class StatesData:
    def __init__(self):
        self.database = pandas.read_csv("50_states.csv")
        self.all_states = self.database.state.tolist()

    def check_guess(self, guessed_state_name):
        guess = self.database[self.database["state"] == guessed_state_name]
        values = guess.values.tolist()
        if values:
            return values
        return []

    def get_missed_states(self, guessed_states):
        missed_states = []
        for state in self.all_states:
            if state in guessed_states:
                missed_states.append(state)
        return missed_states
