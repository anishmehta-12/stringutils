"""Small collection of string utility functions."""


def reverse_words(text):
    """Reverse the order of words in a string."""
    return " ".join(reversed(text.split()))


def title_case(text):
    """Capitalize the first letter of every word."""
    return " ".join(word.capitalize() for word in text.split())


def is_palindrome(text):
    """Check whether a string reads the same forwards and backwards,
    ignoring case, spaces, and punctuation."""
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]
