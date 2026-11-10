
from hypothesis import given, strategies as st
from spam_scoring import sender_domain, first_link, shout_ratio


# 1. Test sender_domain with random inputs
@given(st.text() | st.none())
def test_sender_domain_no_crash(s):
    try:
        sender_domain(s)
    except Exception as e:
        assert False, f"sender_domain crashed with input {s!r}: {e}"


# 2. Test first_link with random inputs
@given(st.text() | st.none())
def test_first_link_no_crash(s):
    try:
        first_link(s)
    except Exception as e:
        assert False, f"first_link crashed with input {s!r}: {e}"


# 3. Test shout_ratio with random inputs
@given(st.text() | st.none())
def test_shout_ratio_no_crash(s):
    try:
        shout_ratio(s)
    except Exception as e:
        assert False, f"shout_ratio crashed with input {s!r}: {e}"
