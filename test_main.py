from main import add, greet

def test_add():
    assert add(10, 20) == 30

def test_greet():
    assert greet() == "Hello from GitHub Actions!"