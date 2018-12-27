# Function prototype
# def control_loop(target_x, target_y)

x_values = [1, 3.5, 6]
y_values = [0, -2.1, 2]

def shape_move(x_values, y_values, num_points):
    number_chooser = 0
    for x in xrange(num_points):
        print (x_values[number_chooser], y_values[number_chooser])
        number_chooser += 1

    # move in shape

def move_triangle(x_center, y_center, length):
    radius_sq = length**2.0 / 3.0
    height_sq = length**2.0 / 4.0
    x_values = []
    y_values = []

    x1 = int(x_center) + 0.0
    x_values.append(x1)
    y1 = int(y_center) + radius_sq**(0.5)
    y_values.append(y1)

    x2 = int(x_center) + length / 2.0
    x_values.append(x2)
    y2 = int(y_center) - (radius_sq - height_sq)**(0.5)
    y_values.append(y2)

    x3 = int(x_center) - length / 2.0
    x_values.append(x3)
    y3 = int(y_center) - (radius_sq - height_sq)**(0.5)
    y_values.append(y3)

    shape_move(x_values, y_values, 3)

    # move in equilateral triangle

move_triangle(0, 0, 3)