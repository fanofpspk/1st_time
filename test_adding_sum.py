import adding_sum  # Import your Python script

def test_addition():
    assert adding_sum.add_numbers(3, 4) == 7
    assert adding_sum.add_numbers(-1, 1) == 0
    assert adding_sum.add_numbers(0, 0) == 0

if __name__ == "__main__":
    test_addition()
    print("All tests passed!")
