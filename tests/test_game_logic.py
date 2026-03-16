from logic_utils import check_guess, get_range_for_difficulty


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# Bug 1: Difficulty ranges must match their intended bounds
def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20


def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 100


def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 50


# Bug 2: check_guess must use numeric comparison, not string comparison
def test_numeric_comparison_not_string():
    # "9" > "50" is True in string comparison, but 9 < 50 numerically
    outcome, message = check_guess(9, 50)
    assert outcome == "Too Low"


def test_numeric_comparison_high():
    # "12" < "9" is True in string comparison, but 12 > 9 numerically
    outcome, message = check_guess(12, 9)
    assert outcome == "Too High"
