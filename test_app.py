from app import classify_review, normalize_review


def test_uppercase_input():
    assert normalize_review("GOOD VALUE FOR MONEY") == "good value for money"


def test_surrounding_whitespace():
    assert normalize_review("\t  Nice and good  \n") == "nice and good"


def test_review_without_keyword_is_unknown():
    assert classify_review("Delivered yesterday") == "unknown"


if __name__ == "__main__":
    tests = [v for k, v in dict(globals()).items() if k.startswith("test_")]
    for t in tests:
        t()
    print(f"{len(tests)} tests passed")
