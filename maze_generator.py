import random

maze = [['1' for _ in range(99)] for _ in range(99)]
path_index = []


#Middle Coord is index 49, 49

direction_length = random.randint(30,40)
XY = True
position = [0,0]

def generate_path(num):
    global XY, direction_length, position, path_index
    for _ in range(direction_length):
        if XY:
            x_direction = random.randint(0,6)
            x_distance = random.randint(1,7)
            if not(x_direction):
                x_distance = min(position[0],x_distance)
                X = position[0]
                position[0] -= x_distance
                while X != position[0] and maze[position[1]][X] != 'P':
                    maze[position[1]][X] = num
                    path_index.append([X, position[1]])
                    X -= 1

            else:
                x_distance = min(98-position[0],x_distance)
                X = position[0]
                position[0] += x_distance
                while X != position[0] and maze[position[1]][X] != 'P':
                    maze[position[1]][X] = num
                    path_index.append([X, position[1]])
                    X += 1
            XY = False
        else:
            y_direction = random.randint(0,6)
            y_distance = random.randint(1,7)
            if not(y_direction):
                y_distance = min(position[1],y_distance)
                Y = position[1]
                position[1] -= y_distance
                while Y != position[1] and maze[Y][position[0]] != 'P':
                    maze[Y][position[0]] = num
                    path_index.append([position[0], Y])
                    Y -= 1
            else:
                y_distance = min(98-position[1],y_distance)
                Y = position[1]
                position[1] += y_distance
                while Y != position[1] and maze[Y][position[0]] != 'P':
                    maze[Y][position[0]] = num
                    path_index.append([position[0], Y])
                    Y += 1
            XY = True

generate_path("P")
while position[0] < 49:
    maze[position[1]][position[0]] = 'P'
    position[0] += 1
while position[0] > 49:
    maze[position[1]][position[0]] = 'P'
    position[0] -= 1
while position[1] < 49:
    maze[position[1]][position[0]] = 'P'
    position[1] += 1
while position[1] > 49:
    maze[position[1]][position[0]] = 'P'
    position[1] -= 1

for i in range(0, len(path_index), 6):
    position = path_index[i]
    direction_length = random.randint(10,15)
    XY = False
    generate_path("S")


for a in maze:
    temp = ""
    for b in a:
        temp += b
    print(temp)

maze[49][49] = 3



            








