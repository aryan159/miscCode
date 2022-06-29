from math import sqrt, atan2

'''
Should we just redo the whole thing? All we have to do is
1. Find the number of layers to generate
2. Generate the x,y of enemies and friendlies, v simple formula
3. Generate dict of angles:dist for each enemy if dist<distance
    If not in dict -> insert
    If in dict -> set distance to shorter one
4. Generate angles of friendles -> if same as dict and distance shorter, remove that entry
5. Return size of dict
6. ???
7. Profit
'''

def solution(dimensions, your_position, trainer_position, distance):
    def addNegatives(l):
        l += [-i for i in l]
        
    numOfLayers = distance / min(dimensions[0], dimensions[1]) + 1
    # i (even) -> (i%2) + 2 == 2 -> return x * (-1)**((i%2)+2) -> x
    # i (odd) -> (i%2) + 2 == 3 -> return x * (-1)**((i%2)+2) -> -x

    # 0, 1, 2, 3, 4, 5
    # 1, 2, 3, 4, 5, 6
    # 0, 2, 2, 4, 4, 6
    trainer_x = [
        dimensions[0] * ((i + 1) / 2) * 2
        + trainer_position[0] * ((-1) ** ((i % 2) + 2)) for i in range(numOfLayers)
        ]
    trainer_y = [
        dimensions[1] * ((i + 1) / 2) * 2
        + trainer_position[1] * ((-1) ** ((i % 2) + 2)) for i in range(numOfLayers)
        ]
    your_x = [
        dimensions[0] * ((i + 1) / 2) * 2
        + your_position[0] * ((-1) ** ((i % 2) + 2)) for i in range(numOfLayers)
        ]
    your_y = [
        dimensions[1] * ((i + 1) / 2) * 2
        + your_position[1] * ((-1) ** ((i % 2) + 2)) for i in range(numOfLayers)
        ]

    addNegatives(trainer_x)
    addNegatives(trainer_y)
    addNegatives(your_x)
    addNegatives(your_y)

    dic = {}
    for x in trainer_x:
        for y in trainer_y:
            x_diff = x - your_position[0]
            y_diff = y - your_position[1]
            length = ((x_diff**2) + (y_diff**2))**(0.5)
            if length <= distance:
                if atan2(y_diff, x_diff) not in dic:
                    dic[atan2(y_diff, x_diff)] = length
                else:
                    dic[atan2(y_diff, x_diff)] = min(length, dic[atan2(y_diff, x_diff)])

    for x in your_x:
        for y in your_y:
            if [x, y] == your_position:
                continue
            x_diff = x - your_position[0]
            y_diff = y - your_position[1]
            if atan2(y_diff, x_diff) in dic:
                length = ((x_diff**2) + (y_diff**2))**(0.5)
                if length < dic[atan2(y_diff, x_diff)]: 
                    del dic[atan2(y_diff, x_diff)]

    return (len(dic))
            
print(solution([3,2], [1,1], [2,1], 3000))
print(solution([300,275], [150,150], [185,100], 500))
#print(solution([3, 4], [1, 1], [2, 3], 20))



