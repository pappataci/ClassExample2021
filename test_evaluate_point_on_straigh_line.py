import pytest

testdata = [ (  ( 1.0 , 1.0 ) , (2.0 , 2.0 ) , 3.0  , 3.0 ) , 
             (  ( 1.0 , 1.0 ) , (1.0 , 2.0 ) , 3.0  , "please provide two different x" ) ,
             (  ( 1.0 , 1.0 ) , (2.0 , 1.0 ) , 3.0  , 1.0 )  ] 

@pytest.mark.parametrize("first_point, second_point, test_point, expected", testdata ) 
def test_estimate_value_of_y_on_straight_line_defined_by_first_two_points(first_point , second_point, test_point, expected ):
    from planar_math import estimate_value_of_y_on_straight_line_defined_by_first_two_points
    answer = estimate_value_of_y_on_straight_line_defined_by_first_two_points(first_point, second_point, test_point)
    assert answer == expected