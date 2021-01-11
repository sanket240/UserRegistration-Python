from user_registration import UserRegistration

user = UserRegistration()


def test_first_name_when_proper_should_return_happy():
    assert user.first_name_validation("Sanket") == "Happy"


def test_first_name_when_improper_should_return_sad():
    assert user.first_name_validation("Sa") == "Sad"


def test_last_name_when_proper_should_return_happy():
    assert user.last_name_validation("Dulange") == "Happy"


def test_last_name_when_improper_should_return_sad():
    assert user.last_name_validation("Du") == "Sad"
