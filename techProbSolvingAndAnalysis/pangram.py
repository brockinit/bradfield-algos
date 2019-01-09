import string
import time

'''
  Assumptions:
   - Phrase will only contain alphabetic characters
'''

pangrams = [
    "the quick brown fox jumps over the lazy dog",
    "Pack my box with five dozen liquor jugs"
]
non_pangrams = [
    "I am not a pangram",
    "no gram of pan here"
]

# O(n^2) quadratic time solution
# Will iterate once for every character in the phrase
# T(n) = 26
def is_pangram_quadratic(phrase):
    start = time.time()
    alphabet = string.ascii_lowercase
    for char in phrase.lower():
        if char in alphabet:
            alphabet = alphabet.replace(char, "")
    end = time.time()
    print("Quadratic:", end - start)
    return len(alphabet) == 0

# O(n^2) quadratic time solution
# Always will iterate 26 times
def is_pangram_quadratic2(phrase):
    start = time.time()
    alphabet = string.ascii_lowercase
    for letter in alphabet:
        if letter in phrase.lower():
            alphabet = alphabet.replace(letter, "")
    end = time.time()
    print("Quadratic:", end - start)
    return len(alphabet) == 0

# O(1) constant time solution
def is_pangram_constant(phrase):
    start = time.time()
    alphabet = string.ascii_lowercase
    chars = set(phrase.lower().replace(" ", ""))
    if len(chars) == len(alphabet):
        end = time.time()
        print("Constant:", end - start)
        return True
    end = time.time()
    print("Constant:", end - start)
    return False


# Tests
for pangram in pangrams:
    assert is_pangram_quadratic(pangram), "{} is not a pangram".format(pangram)
    assert is_pangram_quadratic2(pangram), "{} is not a pangram".format(pangram)
    assert is_pangram_constant(pangram), "{} is not a pangram".format(pangram)

for non_pangram in non_pangrams:
    assert not is_pangram_quadratic(non_pangram), "{} is not a pangram".format(non_pangram)
    assert not is_pangram_quadratic2(non_pangram), "{} is not a pangram".format(non_pangram)
    assert not is_pangram_constant(non_pangram), "{} is not a pangram".format(non_pangram)