import string
import time

pangram = "the quick brown fox jumps over the lazy dog"

# O(n) linear time solution
# Will iterate once for every character in the phrase
def is_pangram_linear1(phrase):
    start = time.time()
    alphabet = string.ascii_lowercase
    for char in phrase:
        if char in alphabet:
            alphabet = alphabet.replace(char, "")
    end = time.time()
    print("Linear1:", end - start)
    return len(alphabet) == 0

is_pangram_linear1(pangram)

# O(n) linear time solution
# Always will iterate 26 times
def is_pangram_linear2(phrase):
    start = time.time()
    alphabet = string.ascii_lowercase
    for letter in alphabet:
        if letter in phrase:
            alphabet = alphabet.replace(letter, "")
    end = time.time()
    print("Linear2:", end - start)
    return len(alphabet) == 0

is_pangram_linear2(pangram)

# O(n^2) quadratic time solution
def is_pangram_quadratic(phrase):
    start = time.time()
    alphabet = string.ascii_lowercase
    for letter in alphabet:
        for char in phrase:
            if char == letter:
                alphabet = alphabet.replace(letter, "")
    end = time.time()
    print("Quadratic:", end - start)
    return len(alphabet) == 0

is_pangram_quadratic(pangram)

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

is_pangram_constant(pangram)