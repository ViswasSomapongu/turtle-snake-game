from food import Food
import random
import time

class Specialfood(Food):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("red")
        self.score_adder = 5
        self.hide()
        self.probability_range = (0.5, 0.8)
        self.start_time = 0
        self.stretch_len_values = [1.0, 1.5]
        self.stretch_wid_values = [1.0, 1.5]
        self.current_size_index = 0

    def hide(self):
        self.goto(1000, 1000)

    def show(self):
        self.refresh()
        self.showturtle()

    def spawn_special_food(self):
        if self.probability_range[0] <= random.random() <= self.probability_range[1]:
            self.show()
            self.start_time = time.time()
            self.toggle_size()

    def toggle_size(self):
        self.current_size_index = 1 - self.current_size_index
        self.shapesize(stretch_len=self.stretch_len_values[self.current_size_index],
                       stretch_wid=self.stretch_wid_values[self.current_size_index])






