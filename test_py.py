from user_registration import UserRegistration

user = UserRegistration()


def test_first_name_when_proper_should_return_happy():
    assert user.get_first_name("Sanket") == "Happy"


def test_first_name_when_improper_should_return_sad():
    assert user.get_first_name("Sa") == "Sad"
