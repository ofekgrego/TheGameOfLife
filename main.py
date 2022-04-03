# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
# https://www.youtube.com/watch?v=FWSR_7kZuYg
from tkinter import *
from GlobalVars import v
import Functions as f

print(v.grid)

v.root = Tk()
v.root.title("The Game of Life")
v.root.resizable(False, False)
v.root.geometry(str(v.window_size_x) + "x" + str(v.window_size_y))
v.canvas = Canvas(v.root, width=v.window_size_x, height=v.window_size_y, background="white")
v.canvas.bind('<Button-1>', f.MousePressed)
v.canvas.pack()

for i in range(v.rows_columns_num):
    v.canvas.create_line(0, i*(v.window_size_x/ v.rows_columns_num),v.window_size_y,i*(v.window_size_x/ v.rows_columns_num),fill="#000")
    v.canvas.create_line(i * (v.window_size_x / v.rows_columns_num),0, i * (v.window_size_y /  v.rows_columns_num),v.window_size_x, fill="#000")

v.root.mainloop()