import turtle


class State(turtle.Turtle):
    def __init__(self, coordinates, state):
        super().__init__()
        self.name = state
        self.penup()
        self.hideturtle()
        self.goto(coordinates)
        self.write(arg=state)


class Map:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("U.S. States Game")
        self.screen.screensize(canvwidth=725, canvheight=491)
        self.screen.bgpic("blank_states_img.gif")
        self.screen.tracer(0)
        self.guessed_states = []
        self.states = {}

    def get_guess(self):
        return self.screen.textinput(f"{len(self.guessed_states)} / 50 correct!",
                                     "Give me the name of a state from US:").title()

    def set_exit(self):
        self.screen.exitonclick()

    def reveal_state(self, coordinate, name):
        state = State(coordinate, name)
        if name not in self.guessed_states:
            self.guessed_states.append(name)
            self.states[name] = state
            self.screen.update()

    def is_game_over(self):
        return len(self.guessed_states) == 50