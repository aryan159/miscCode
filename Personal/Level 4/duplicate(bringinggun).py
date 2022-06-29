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
        dist = ((v[0])**2 + (v[1])**2)**(0.5)
        return dist <= distance
        
    # Solution Starts Here
    dimensions[0] = Fraction(dimensions[0], 1)
    dimensions[1] = Fraction(dimensions[1], 1)
    your_position[0] = Fraction(your_position[0], 1)
    your_position[1] = Fraction(your_position[1], 1)
    trainer_position[0] = Fraction(trainer_position[0], 1)
    trainer_position[1] = Fraction(trainer_position[1], 1)
    distance = Fraction(distance, 1)

    # Initialize 2 dictionaries that store angle:dist 
    self_angles = {}
    enemy_angles = {}

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

print(solution([3,2], [1,1], [2,1], 4))
print(solution([300,275], [150,150], [185,100], 500))
#print(solution([30,27], [19,22], [15,16], 700))
#print(solution([54,92], [45,34], [13,18], 700))
print(solution([15,10], [8,2], [7,5], 400))
#print(solution([3, 3], [1, 1], [2, 2], 1000))