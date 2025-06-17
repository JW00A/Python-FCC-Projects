** start of main.py **

import copy
import random

class Hat:
    def __init__(self, **args):
        self.contents = []
        for color, count in args.items():
            self.contents.extend([color] * count)
    
    def draw(self, num):
        if num > len(self.contents):
            contents = self.contents
            self.contents = []

            return contents

        contents = []
        for i in range(0, num):
            choice = random.choice(self.contents)
            
            contents.append(choice)
            self.contents.remove(choice)
        
        return contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    N = num_experiments

    M = 0
    for _ in range(N):
        new_hat = copy.deepcopy(hat)
        draws = new_hat.draw(num_balls_drawn)
        draw_counts = {}

        for color in draws:
            draw_counts[color] = draw_counts.get(color, 0) + 1

        success = True
        for color, count in expected_balls.items():
            if draw_counts.get(color, 0) < count:
                success = False
                break

        if (success):
            M += 1
    
    probability = M / N
    return probability

hat = Hat(black=6, red=4, green=3)

probability = experiment(hat = hat, 
                         expected_balls = {'red': 2, 'green': 1}, 
                         num_balls_drawn = 5, 
                         num_experiments = 2000)
print(probability)

** end of main.py **

