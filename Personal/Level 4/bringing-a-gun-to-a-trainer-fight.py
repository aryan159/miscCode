import time
from fractions import Fraction

def solution(dimensions, your_position, trainer_position, distance):
    # Dimensions -> x,y | You -> x1,y1 | Trainer -> x2,y2 | Distance -> d
    # Using a nested for loop, generate all possible vectors that will hit the enemy without hitting you or any corner
    # x_dist (right) -> x-x1 + x-x2 | x-x1 + x + x2 | x-x1 + 2x + x-x2 | {x-x1 + nx + [x-x2 if even, x2 if odd]} 
    # x_dist (left) -> x1 + x2 | x1 + x + x-x2 | x1 + 2x + x2 | {x1 + nx + [x2 if even, x-x2 if odd]}
    # x_dist (base_case) -> x2 - x1
    
    # y_dist (up) -> y-y1 + y-y2 | y-y1 + y + y2 | {y-y1 + ny + [y-y2 if even, y2 if odd]} 
    # y_dist (down) -> {y1 + ny + [y2 if even, y-y2 if odd]}
    # y_dist (base_case) -> y2 - y1

    def valid(v):
        #print('valid(' + str(v[0]) + ',' + str(v[1]) + ')')
        corners = [
            [0, 0],
            [0, dimensions[1]],
            [dimensions[0], 0],
            [dimensions[0], dimensions[1]]
        ]

        
        pos = your_position

        '''while True:

            # Check if we are hitting ourselves
            hitting_ourselvs = False
            if pos != your_position:
                x_time_ourselves = (your_position[0] - pos[0]) / v[0]
                y_time_ourselves = (your_position[1] - pos[1]) / v[1]
                if x_time == y_time and x_time > 0:
                    hitting_ourselvs = True
                    print('[HITTING OURSELVES!]')


            # Check if we are hitting the trainer
            x_satisfied = False
            try:
                x_time = (trainer_position[0] - pos[0]) / v[0]
            except:
                x_satisfied = True
                x_time = 0
            y_satisfied = False
            try:
                y_time = (trainer_position[1] - pos[1]) / v[1]
            except:
                y_satisfied = True
                y_time = 0
            if (x_time == y_time or (x_satisfied and y_time > 0) or (y_satisfied and x_time > 0)):
                break

            # Check which wall we are hitting
            horizontal = True

            dist_to_x = -1
            if v[0] < 0:
                dist_to_x = pos[0] / (v[0] * -1)
            elif v[0] > 0:
                dist_to_x = (dimensions[0] - pos[0]) / v[0]

            dist_to_y = -1
            if v[1] < 0:
                dist_to_y = pos[1] / (v[1] * -1)
            elif v[1] > 0:
                dist_to_y = (dimensions[1] - pos[1]) / v[1]

            horizontal = (dist_to_x < dist_to_y)
            if dist_to_x == -1: horizontal = False
            if dist_to_y == -1: horizontal = True

            if horizontal:
                if v[0] < 0:
                    newPos = [0, pos[1] + (v[1] * ((0 - pos[0]) / v[0]))]
                elif v[0] > 0:
                    newPos = [dimensions[0], pos[1] + (v[1] * ((dimensions[0] - pos[0]) / v[0]))]
                else:
                    print("[horizontal] SOMETHING V WRONG HAS HAPPENED")
            else:
                if v[1] < 0:
                    newPos = [pos[0] + (v[0] * ((0 - pos[1]) / v[1])), 0]
                elif v[1] > 0:
                    newPos = [pos[0] + (v[0] * ((dimensions[1] - pos[1]) / v[1])), dimensions[1]]
                else:
                    print("[!horizontal] SOMETHING V WRONG HAS HAPPENED")

            # Check if we have hit any corner
            for corner in corners:
                if newPos == corner:
                    # print('[HITTING CORNER!]')
                    return False

            # Set variables for next loop
            v = [v[0]*-1, v[1]] if horizontal else [v[0], v[1]*-1]
            pos = newPos'''

        
        # Calculate Distance
        dist = (v[0]**2 + v[1]**2)**0.5
        if dist < distance:
            return True
        else: 
            return False
        
    # Solution Starts Here
    dimensions[0] = Fraction(dimensions[0], 1)
    dimensions[1] = Fraction(dimensions[1], 1)
    your_position[0] = Fraction(your_position[0], 1)
    your_position[1] = Fraction(your_position[1], 1)
    trainer_position[0] = Fraction(trainer_position[0], 1)
    trainer_position[1] = Fraction(trainer_position[1], 1)
    distance = Fraction(distance, 1)

    ans = 0
    x_inc = -1
    y_inc = -1
    x_base = trainer_position[0] - your_position[0]
    if x_base == 0:
        if valid([x_base, 1]): ans += 1
        x_base = None
    y_base = trainer_position[1] - your_position[1]
    if y_base == 0:
        if valid([1, y_base]): ans += 1
        y_base = None
    # x
    while True:
        x_right = dimensions[0] - your_position[0] + x_inc * dimensions[0]
        if x_inc % 2 == 0:
            x_right += dimensions[0] - trainer_position[0]
        else:
            x_right += trainer_position[0]

        x_left = your_position[0] + x_inc * dimensions[0]
        if x_inc % 2 == 0:
            x_left += trainer_position[0]
        else:
            x_left += dimensions[0] - trainer_position[0]
        x_left *= -1

        previous_ans = ans

        # y
        y_inc = -1
        while True:
            y_up = dimensions[1] - your_position[1] + y_inc * dimensions[1]
            if y_inc % 2 == 0:
                y_up += dimensions[1] - trainer_position[1]
            else:
                y_up += trainer_position[1]

            y_down = your_position[1] + y_inc * dimensions[1]
            if y_inc % 2 == 0:
                y_down += trainer_position[1]
            else:
                y_down += dimensions[1] - trainer_position[1]
            y_down *= -1

            prev_ans = ans

            if x_inc == -1 and y_inc != -1 and x_base:
                if valid([x_base, y_up]): ans += 1
                if valid([x_base, y_down]): ans += 1
            if x_inc != -1 and y_inc == -1 and y_base:
                if valid([x_right, y_base]): ans += 1
                if valid([x_left, y_base]): ans += 1
            if x_inc == -1 and y_inc == -1 and x_base and y_base:
                if valid([x_base, y_base]): ans += 1
            if x_inc != -1 and y_inc != -1:
                if valid([x_right, y_up]): ans += 1
                if valid([x_right, y_down]): ans += 1
                if valid([x_left, y_up]): ans += 1
                if valid([x_left, y_down]): ans += 1

            if prev_ans == ans and not (y_inc == -1 and not y_base):
                break

            y_inc += 1

        # All cases exhausted
        if previous_ans == ans and not (x_inc == -1 and not x_base):
            break

        x_inc += 1

    return ans

import time
start_time = time.time()
print(solution([3,2], [1,1], [2,1], 4))
print(solution([300,275], [150,150], [185,100], 500))
print(solution([3, 3], [1, 1], [2, 2], 1000))
print("--- %s seconds ---" % (time.time() - start_time))


