def reverse_string(s):
    return s[::-1]

def is_palindrome(word):
    cleaned_word = ''.join(word.lower().split())
    return cleaned_word == cleaned_word[::-1]

def extract_vowels(input_string):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in input_string if char in vowels])

def remove_dublicate(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)