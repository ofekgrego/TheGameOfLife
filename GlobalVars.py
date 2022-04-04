
class v(object):
    window_size_x = 500
    window_size_y = 500

    rows_columns_num = 25

    auto_move = False
    auto_move_func = None

    grid = []
    grid_of_objects = []
    for x in range(0, rows_columns_num):
        row = []
        row2 = []
        for x in range(0, rows_columns_num):
            row.append(0)
            row2.append(0)
        grid.append(row)
        grid_of_objects.append(row2)


    root = None
    canvas = None