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


def test_email_when_proper_should_return_happy():
    assert user.email_validation("sanketdulange24@gmail.com") == "Happy"


def test_email_when_improper_should_return_sad():
    assert user.email_validation("sank.gmail.com") == "Sad"


def test_phone_number_when_proper_should_return_happy():
    assert user.phone_number_validation("91 9422484996") == "Happy"


def test_phone_number_improper_should_return_sad():
    assert user.phone_number_validation("9422484996") == "Sad"


def test_password_rule4_when_proper_should_return_happy():
    assert user.password_validation("Sanket$1") == "Happy"


def test_password_rule4_improper_should_return_sad():
    assert user.password_validation("sany") == "Sad"
