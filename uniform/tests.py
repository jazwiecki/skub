import uniform

# TODO: test excluding non-alpha chars
# TODO: refactor uniform to take a set of regexes for exclusion/replacement?
# TODO: test @-mentions
# TODO: test #channels

def test_transform():
    expected_string = "𝕒𝕓𝕔"
    test_submission = "abc"

    results = uniform.transform(test_submission, "hollow")
    assert expected_string == results