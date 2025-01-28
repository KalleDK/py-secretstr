from secretstr import SecretStr


def test_print():
    s = SecretStr("password")
    assert str(s) == "**********"
    assert repr(s) == "SecretStr('**********')"
    assert len(s) == 8
    assert s.get_secret_value() == "password"
    assert s == SecretStr("password")
    assert s != SecretStr("password1")
    assert hash(s) == hash(SecretStr("password"))
    assert hash(s) != hash(SecretStr("password1"))
