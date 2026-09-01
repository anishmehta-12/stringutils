from stringutils import reverse_words, title_case


def test_reverse_words():
    assert reverse_words("the quick brown fox") == "fox brown quick the"


def test_title_case():
    assert title_case("hello world") == "Hello World"
