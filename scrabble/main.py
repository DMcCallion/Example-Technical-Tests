import random

LETTER_VALUES = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
}

def get_bag():
    return {
    'E': 12,
    'A': 9, 'I': 9,
    'O': 8,
    'N': 6, 'R': 6, 'T': 6,
    'L': 4, 'S': 4, 'U': 4, 'D': 4,
    'G': 3,
    'B': 2, 'C': 2, 'M': 2, 'P': 2, 'F': 2,
    'H': 2, 'V': 2, 'W': 2, 'Y': 2,
    'K': 1, 'J': 1, 'X': 1, 'Q': 1, 'Z': 1
}

def get_score(word):
    score = 0
    word = word.upper()
    for letter in word:
        score += LETTER_VALUES[letter]
    
    return score

def assign_letters(bag):
    alphabet = [letter for letter in LETTER_VALUES.keys()]
    letters = []
    while len(letters) < 7:
        choice = random.randint(0, 25)
        letter =alphabet[choice]
        
        if bag[letter] > 0:
            bag[letter] -= 1
            letters.append(letter)
        else:
            continue

    return letters
    

def find_valid_word(letters):
    with open("dictionary.txt", "r") as f:
        words = f.readlines()
    
    for word in words:
        match = True
        for letter in word:
            if letter not in letters:
                match = False
                break
        if match: 
            return word
    return ""    

if __name__ == "__main__":
    random.seed(12)
    print(assign_letters())

