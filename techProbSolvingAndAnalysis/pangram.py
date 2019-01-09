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

'''
  For this solution, I iterate over each letter in the alphabet and check if
  it exists in the phrase. If so, I remove the letter from the alphabet string.
  If the phrase is a pangram, the alphabet string will be empty at the end.

  T(n) = 26n + 6

  This solution has an average case of O(n), because the alphabet is a constant,
  but we don't know how long the phrase (n) will be.
'''
def is_pangram_linear1(phrase):
    start = time.time()
    alphabet = string.ascii_lowercase
    phrase = phrase.lower()
    for letter in alphabet:
        if letter in phrase:
            alphabet = alphabet.replace(letter, "")
    end = time.time()
    print("Linear1:", end - start)
    return len(alphabet) == 0

'''
  In this solution, I reduce the phrase down to a string of unique alphabetic
  characters. If the length of this string is 26, we know that the original phrase
  is a pangram.

  T(n) = 3n + 6

  This solution has an average case of O(n) because of the use of set, str.lower, and str.replace,
  each of which have to iterate n times to traverse the phrase.
'''
def is_pangram_linear2(phrase):
    start = time.time()
    alphabet = string.ascii_lowercase
    chars = set(phrase.lower().replace(" ", ""))
    if len(chars) == len(alphabet):
        end = time.time()
        print("Linear2:", end - start)
        return True
    end = time.time()
    print("Linear2:", end - start)
    return False

'''
  In this solution, take the phrase and convert it to a set so that it only
  contains unique characters (spaces omitted). I then convert the set back to a list so
  that it can be sorted and finally converted back to a string. At this point, the string will
  either be equal to the alphabet string if it is indeed a pangram.

  T(n) = 6n + 5

  This solution has an average case of O(n) because each of the python functions used
  requires n iterations to complete.
'''
def is_pangram_linear3(phrase):
    start = time.time()
    alphabet = string.ascii_lowercase
    phrase = "".join(sorted(list(set(phrase.lower().replace(" ", "")))))
    end = time.time()
    print("Linear3:", end - start)
    return alphabet == phrase

# Tests
for pangram in pangrams:
    assert is_pangram_linear1(pangram), "{} is not a pangram".format(pangram)
    assert is_pangram_linear2(pangram), "{} is not a pangram".format(pangram)
    assert is_pangram_linear3(pangram), "{} is not a pangram".format(pangram)

for non_pangram in non_pangrams:
    assert not is_pangram_linear1(non_pangram), "{} is not a pangram".format(non_pangram)
    assert not is_pangram_linear2(non_pangram), "{} is not a pangram".format(non_pangram)
    assert not is_pangram_linear3(non_pangram), "{} is not a pangram".format(non_pangram)