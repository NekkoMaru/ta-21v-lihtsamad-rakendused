map = [
    [12, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 1, 0],
    [24, 0, 1, 0, 0],
    [1, 1, 1, 1, 1]
]

start_pos_x = 0
start_pos_y = 0

y_rows = 5
x_columns = 5

def get_next_free_position(current_possition_y, current_position_x):
    if current_position_x+1 < x_columns and map[current_possition_y][current_position_x+1] == 1:
        print("can go right")
        return[current_possition_y, current_position_x+1]

    if current_possition_y+1 < y_rows and map[current_possition_y+1][current_position_x] == 1:
        print("can go bottom")
        return[current_possition_y+1, current_position_x]

next_free_position = get_next_free_position(start_pos_y, start_pos_x)
print("Next free position is: ", next_free_position)

while next_free_position:
    next_free_position = get_next_free_position(next_free_position[0], next_free_position[1])
    print("Next free position is: ", next_free_position)