def get_value_of_y_in_non_horizontal_straight_line(x1,y1,x2,y2, test_point):
    delta_x = x2 - x1
    delta_y = y2 - y1 
    m = delta_y/delta_x
    return m *(test_point - x1 ) + y1 

def estimate_value_of_y_on_straight_line_defined_by_first_two_points(first_point, second_point, test_point):
    x1 , y1 = first_point
    x2 , y2 = second_point
    if (x1 == x2):
        return 'please provide two different xs'
    else:
        return get_value_of_y_in_non_horizontal_straight_line(x1,y1,x2,y2, test_point)