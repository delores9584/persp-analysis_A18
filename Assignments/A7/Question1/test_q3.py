## Test file for problem 3

import q3, pytest

def test_operate():
    assert q3.operate(1,3,"+") == 4
    assert q3.operate(-1,-3,"+") == -4
    assert q3.operate(1,3,"-") == -2
    assert q3.operate(-1,-3,"-") == 2
    assert q3.operate(5,3,"*") == 15
    assert q3.operate(0,5,"*") == 0
    assert q3.operate(5,3,"/") == 5/3
    
    with pytest.raises(ZeroDivisionError) as err:
        q3.operate(2,0,'/')
    assert err.value.args[0]=="division by zero is undefined"
    
    with pytest.raises(ValueError) as ValErr:
        q3.operate(2,0,'}')
    assert ValErr.value.args[0]=="oper must be one of '+', '/', '-', or '*'"
        
    with pytest.raises(TypeError) as type_err:
        q3.operate(2,3,9)
    assert type_err.value.args[0] == "oper must be a string"
    