from stringutils import is_palindrome, reverse_words, title_case


def test_reverse_words():
    assert reverse_words("the quick brown fox") == "fox brown quick the"


def test_title_case():
    assert title_case("hello world") == "Hello World"


def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("hello world")
