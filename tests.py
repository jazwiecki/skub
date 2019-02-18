import uniform

def test_transform():
    expected_string = "𝕒𝕓𝕔"
    test_submission = "abc"

    results = uniform.transform(test_submission, "hollow")
    assert expected_string == results