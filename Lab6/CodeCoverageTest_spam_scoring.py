
from spam_scoring import score_message, classify, filter_inbox, inbox_status


# 1. SCORE MESSAGE TESTS

def test_spam_keyword():
    assert score_message("free prize", False, 0) == 4


def test_spam_keyword_with_punctuation():
    assert score_message("urgent!", False, 0) == 2


def test_uppercase_words():
    assert score_message("HELLO WORLD", False, 0) == 2


def test_short_uppercase_word():
    assert score_message("YES", False, 0) == 0


def test_link_count_above_three():
    assert score_message("hello", False, 5) == 4


def test_link_count_between_one_and_three():
    assert score_message("hello", False, 2) == 1


def test_known_sender_negative_score():
    assert score_message("hello", True, 0) == 0


def test_known_sender_with_positive_score():
    assert score_message("free prize", True, 0) == 1


# 2. CLASSIFICATION TESTS

def test_classify_spam():
    assert classify(8) == "spam"


def test_classify_suspicious():
    assert classify(4) == "suspicious"


def test_classify_clean():
    assert classify(2) == "clean"


# 3. INBOX FILTER TESTS


def test_filter_inbox_multiple_messages():
    messages = [
        ("free prize urgent winner", False, 0),
        ("free prize", False, 0),
        ("hello", False, 0)
    ]

    assert filter_inbox(messages) == {
        "spam": 1,
        "suspicious": 1,
        "clean": 1
    }

def test_filter_empty_inbox():
    assert filter_inbox([]) == {
        "spam": 0,
        "suspicious": 0,
        "clean": 0
    }


# 4. INBOX STATUS TESTS

def test_empty_inbox_status():
    assert inbox_status({"spam": 0, "suspicious": 0, "clean": 0}) == "empty"


def test_flooded_inbox():
    assert inbox_status({"spam": 6, "suspicious": 2, "clean": 2}) == "flooded"


def test_noisy_inbox():
    assert inbox_status({"spam": 3, "suspicious": 4, "clean": 3}) == "noisy"


def test_healthy_inbox():
    assert inbox_status({"spam": 2, "suspicious": 3, "clean": 5}) == "healthy"
