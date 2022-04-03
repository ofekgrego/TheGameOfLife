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