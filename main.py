# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
# https://www.youtube.com/watch?v=FWSR_7kZuYg
from tkinter import *

window_size_x = 500
window_size_y = 500

rows_columns_num = 10


root = Tk()
root.title("The Game of Life")
root.resizable(False, False)
root.geometry(str(window_size_x) + "x" + str(window_size_y))
canvas = Canvas(root, width=window_size_x, height=window_size_y, background="white")
canvas.pack()

for i in range(rows_columns_num):
    canvas.create_line(0, i*(window_size_x/rows_columns_num),window_size_y,i*(window_size_x/rows_columns_num),fill="#000")
    canvas.create_line(i * (window_size_y / rows_columns_num),0, i * (window_size_y / rows_columns_num),window_size_x, fill="#000")



root.mainloop()