import pytest

@pytest.mark.parametrize("hdl_number, expected", [(65, 'Normal'), (40, 'Borderline Low') , (25, 'Low')] ) 
def test_analyze_HDL_Normal(hdl_number , expected):
    from blood_tests import analyze_HDL
    answer = analyze_HDL(hdl_number)
    assert answer == expected