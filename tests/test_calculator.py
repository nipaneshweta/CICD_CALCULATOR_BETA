from app.calculator import add, substract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    
def test_substract():
    assert substract(5, 2) == 3
    
def test_multiply():
    assert multiply(2, 4) == 8 
    
def test_divide():
    assert divide(10, 2) == 5