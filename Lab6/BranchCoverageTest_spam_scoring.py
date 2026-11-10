
from spam_scoring import score_message, classify, filter_inbox, inbox_status


# 1. SCORE MESSAGE – BRANCH TESTS

def test_empty_message():
    assert score_message("", False, 0) == 0


def test_spam_word_branch():
    assert score_message("free", False, 0) == 2


def test_non_spam_uppercase_branch():
    assert score_message("HELLO", False, 0) == 1


def test_non_spam_lowercase_branch():
    assert score_message("hello", False, 0) == 0


def test_multiple_spam_words():
    assert score_message("free winner prize urgent cash", False, 0) == 10


def test_link_count_greater_than_three():
    assert score_message("hello", False, 4) == 4


def test_link_count_between_one_and_three():
    assert score_message("hello", False, 2) == 1


def test_zero_links():
    assert score_message("hello", False, 0) == 0


def test_known_sender_score_below_zero():
    assert score_message("hello", True, 0) == 0


def test_known_sender_score_above_zero():
    assert score_message("free prize", True, 0) == 1


def test_unknown_sender():
    assert score_message("free", False, 0) == 2


# 2. CLASSIFICATION – BRANCH TESTS

def test_spam_boundary():
    assert classify(8) == "spam"


def test_below_spam_boundary():
    assert classify(7) == "suspicious"


def test_suspicious_boundary():
    assert classify(4) == "suspicious"


def test_below_suspicious_boundary():
    assert classify(3) == "clean"


# 3. FILTER INBOX – BRANCH TESTS

def test_empty_inbox_filter():
    assert filter_inbox([]) == {
        "spam": 0,
        "suspicious": 0,
        "clean": 0
    }


def test_inbox_with_messages():
    messages = [
        ("free winner prize urgent", False, 0),
        ("free prize", False, 0),
        ("hello", False, 0)
    ]

    assert filter_inbox(messages) == {
        "spam": 1,
        "suspicious": 1,
        "clean": 1
    }


# 4. INBOX STATUS – BRANCH TESTS

def test_empty_inbox_status():
    assert inbox_status({
        "spam": 0,
        "suspicious": 0,
        "clean": 0
    }) == "empty"


def test_flooded_inbox():
    assert inbox_status({
        "spam": 6,
        "suspicious": 2,
        "clean": 2
    }) == "flooded"


def test_exactly_half_spam():
    assert inbox_status({
        "spam": 5,
        "suspicious": 2,
        "clean": 3
    }) == "noisy"


def test_noisy_inbox():
    assert inbox_status({
        "spam": 3,
        "suspicious": 4,
        "clean": 3
    }) == "noisy"


def test_exactly_twenty_percent_spam():
    assert inbox_status({
        "spam": 2,
        "suspicious": 3,
        "clean": 5
    }) == "healthy"


def test_healthy_inbox():
    assert inbox_status({
        "spam": 1,
        "suspicious": 2,
        "clean": 7
    }) == "healthy"
