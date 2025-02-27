from main import (
    reverse_string,
    is_palindrome,
    extract_vowels,
    remove_dublicate
)

def test_reverse():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("ab") == "ba"
    assert reverse_string("madam") == "madam"
    assert reverse_string("hello world") == "dlrow olleh"
    assert reverse_string("!@#") == "#@!"
    assert reverse_string("123") == "321"
    assert reverse_string("ab12!#") == "#!21ba"
    assert reverse_string("the long string") == "gnirts gnol eht" 

def test_palindrome():
    assert is_palindrome("")
    assert is_palindrome("racecar")
    assert is_palindrome("abba")
    assert is_palindrome("a man a plan a canal panama")
    assert is_palindrome("madam")
    assert is_palindrome("12321")
    assert is_palindrome("noon")
    assert is_palindrome("a")
    assert is_palindrome("was it a cat i saw")
    assert is_palindrome("deified")

def test_vowels():
    assert extract_vowels("bcd") == ""
    assert extract_vowels("aeiouAEIOU") == "aeiouAEIOU"
    assert extract_vowels("Hello World!") == "eoo"
    assert extract_vowels("123!@abcde") == "ae"
    assert extract_vowels("CATANDDOG") == "AAO"
    assert extract_vowels("banana") == "aaa"
    assert extract_vowels("CAT walk") == "Aa"
    assert extract_vowels("a e i o u") == "aeiou"
    assert extract_vowels("A e I o U") == "AeIoU"
    assert extract_vowels("race") == "ae"

def test_dublicates():
    assert remove_dublicate("") == ""
    assert remove_dublicate("a") == "a"
    assert remove_dublicate("aaa") == "a"
    assert remove_dublicate("fox") == "fox"
    assert remove_dublicate("foxandfox") == "foxand"
    assert remove_dublicate("a b c a b") == "a bc"
    assert remove_dublicate("f o x f o x") == "f ox"
    assert remove_dublicate("!@#!@#") == "!@#"
    assert remove_dublicate("longstringwitduplicates") == "longstriwdupcae"