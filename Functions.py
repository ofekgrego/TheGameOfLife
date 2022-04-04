from GlobalVars import v
from tkinter import *
import math

def MousePressed(event):
    global grid,grid_of_objects
    block_size = v.window_size_x/v.rows_columns_num
    pressed_block_x = math.floor(event.x/block_size)
    pressed_block_y = math.floor(event.y / block_size)

    if(v.grid[pressed_block_x][pressed_block_y] == 0):
        v.grid[pressed_block_x][pressed_block_y] = 1
        v.grid_of_objects[pressed_block_x][pressed_block_y] = v.canvas.create_rectangle(pressed_block_x * block_size,
                                  pressed_block_y * block_size,
                                  (pressed_block_x + 1) * block_size
                                  , (pressed_block_y + 1) * block_size, fill="black")
    else:
        v.grid[pressed_block_x][pressed_block_y] = 0
        v.canvas.delete(v.grid_of_objects[pressed_block_x][pressed_block_y])

    CheckNeighbours(pressed_block_x, pressed_block_y)

def CheckNeighbours(place_x,place_y):
    #Check if need to change
    count_of_live_neighbours = 0
    dir = [False,False,False,False] #L R U D
    if(place_x != 0):
        if(v.grid[place_x - 1][place_y] == 1):
            count_of_live_neighbours += 1
            # print("Can Left")
        dir[0] = True
    if (place_x != v.rows_columns_num-1):
        if (v.grid[place_x + 1][place_y] == 1):
            count_of_live_neighbours += 1
            # print("Can Right")
        dir[1] = True
    if(place_y != 0):
        if (v.grid[place_x][place_y - 1] == 1):
            count_of_live_neighbours += 1
            # print("Can Up")
        dir[2] = True
    if (place_y != v.rows_columns_num-1):
        if (v.grid[place_x][place_y + 1] == 1):
            count_of_live_neighbours += 1
            # print("Can Down")
        dir[3] = True

    if(dir[0] & dir[2]):
        if (v.grid[place_x - 1][place_y - 1] == 1):
            count_of_live_neighbours += 1
            # print("Can LeftUp")
    if(dir[1] & dir[2]):
        if (v.grid[place_x + 1][place_y - 1] == 1):
            count_of_live_neighbours += 1
            # print("Can RightUp")
    if(dir[0] & dir[3]):
        if (v.grid[place_x - 1][place_y + 1] == 1):
            count_of_live_neighbours += 1
            # print("Can LeftDown")
    if(dir[1] & dir[3]):
        if (v.grid[place_x + 1][place_y + 1] == 1):
            count_of_live_neighbours += 1
            # print("Can RightDown")
    return count_of_live_neighbours


def MoveGen():
    # move all the tiles a gen
    print("Move Gen")