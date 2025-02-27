import main
import unittest

class TestReverseStrString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(main.reverse_string(""), "")
    def test_single_character(self):
        self.assertEqual(main.reverse_string("a"), "a")
    def test_two_characters(self):
        self.assertEqual(main.reverse_string("ab"), "ba")
    def test_palindrome(self):
        self.assertEqual(main.reverse_string("madam"), "madam")
    def test_regular_string(self):
        self.assertEqual(main.reverse_string("hello"), "olleh")
    def test_string_with_spaces(self):
        self.assertEqual(main.reverse_string("hello world"), "dlrow olleh")
    def test_string_with_spec_chars(self):
        self.assertEqual(main.reverse_string("!@#"), "#@!")
    def test_num_strings(self):
        self.assertEqual(main.reverse_string("123"), "321")
    def test_mix_chars(self):
        self.assertEqual(main.reverse_string("ab12!@"), "@!21ba")
    def test_long_string(self):
        self.assertEqual(main.reverse_string("the long string"), "gnirts gnol eht")

class TestPalindrome(unittest.TestCase):
    def test_palindrome_even_lenght(self):
        self.assertTrue(main.is_palindrome("abba"))
    def test_palindrome_odd_lenght(self):
        self.assertTrue(main.is_palindrome("racecar"))
    def test_not_palindrome(self):
        self.assertFalse(main.is_palindrome("hello"))
    def test_palindrome_with_spaces(self):
        self.assertTrue(main.is_palindrome("A man a plan a canal Panama"))
    def test_palindrome_with_punctuation(self):
        self.assertFalse(main.is_palindrome("Madam, I'm Adam"))
    def test_empty_string(self):
        self.assertTrue(main.is_palindrome(""))
    def test_single_character(self):
        self.assertTrue(main.is_palindrome("a"))
    def test_case_insensitivity(self):
        self.assertTrue(main.is_palindrome("Noon"))
    def test_not_palindrome_with_spec_chars(self):
        self.assertFalse(main.is_palindrome("12345!"))
    def test_palindrome_with_numbers(self):
        self.assertTrue(main.is_palindrome("12321"))

class TestExtractVowels(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(main.extract_vowels(''), '')
    def test_no_vowels(self):
        self.assertEqual(main.extract_vowels("bcd"), "")
    def test_all_vowels(self):
        self.assertEqual(main.extract_vowels("aeiouAEIOU"), "aeiouAEIOU")
    def test_mixed_characters(self):
        self.assertEqual(main.extract_vowels("Hello World!"), "eoo")
    def test_numbers_and_symbols(self):
        self.assertEqual(main.extract_vowels("123abcdo"), "ao")
    def test_case_sensitivity(self):
        self.assertEqual(main.extract_vowels("HellO WOrld"), "eOO")
    def test_repeated_vowels(self):
        self.assertEqual(main.extract_vowels("banana"), "aaa")
    def test_long_string(self):
        self.assertEqual(main.extract_vowels("the long string"), "eoi")
    def test_vowels_with_spaces(self):
        self.assertEqual(main.extract_vowels("a e i o u"), "aeiou")
    def test_spec_characters(self):
        self.assertEqual(main.extract_vowels("#@!"), "")

class TestRemoveDuplicate(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(main.remove_dublicate(""), "")
    def test_single_characeters(self):
        self.assertEqual(main.remove_dublicate("a"), "a")
    def test_all_unique_characeters(self):
        self.assertEqual(main.remove_dublicate("abcde"), "abcde")
    def test_all_dublicate(self):
        self.assertEqual(main.remove_dublicate("aaaaaa"), "a")
    def test_mixed_characters(self):
        self.assertEqual(main.remove_dublicate("abacabad"), "abcd")
    def test_case_sensitivity(self):
        self.assertEqual(main.remove_dublicate("aA"), "aA")
    def test_numerical_characters(self):
        self.assertEqual(main.remove_dublicate("123123"), "123")
    def test_spec_characters(self):
        self.assertEqual(main.remove_dublicate("!@#!@#"), "!@#")
    def test_spaces(self):
        self.assertEqual(main.remove_dublicate("a b c a d"), "a bcd")
    def test_long_string(self):
        self.assertEqual(main.remove_dublicate("longstringwithdublicates"), "longstriwhdubcae")

if __name__ == '__main__':
    unittest.main()