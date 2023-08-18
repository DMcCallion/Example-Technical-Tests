import random
from main import get_score, assign_letters, get_bag, find_valid_word

def test_get_score_guardian():
    assert get_score("GUARDIAN") == 10



def test_assign_letter_length():
    bag = get_bag()
    assert len(assign_letters(bag)) == 7

def test_bag():
    random.seed(12)
    bag = get_bag()
    assert assign_letters(bag) == ['P', 'I', 'V', 'Q', 'V', 'L', 'E']
    
def test_bag_count_changes():
    random.seed(12)
    bag = get_bag()
    
    letters = assign_letters(bag)

    assert bag["V"] == 0


def test_valid_word():
    assert find_valid_word(["a", "a"]) == "aa"

def test_invalid():
    assert find_valid_word(["z"]) == ""