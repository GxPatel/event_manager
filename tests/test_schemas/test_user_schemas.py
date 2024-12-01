from pydantic import ValidationError
import pytest
from app.schemas.user_schemas import UserBase

# Test valid nicknames with boundary values
@pytest.mark.parametrize("nickname", ["usr", "u" * 30])  # Min and max lengths
def test_user_base_nickname_boundary(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    user = UserBase(**user_base_data)
    assert user.nickname == nickname

# Test invalid nicknames for boundary values
@pytest.mark.parametrize("nickname", ["us", "u" * 31])  # Below min and above max
def test_user_base_nickname_boundary_invalid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Test valid bio with max length
def test_user_base_bio_max_length(user_base_data):
    user_base_data["bio"] = "A" * 500  # Max length for bio
    user = UserBase(**user_base_data)
    assert user.bio == "A" * 500

# Test invalid bio with excessive length
def test_user_base_bio_excessive_length(user_base_data):
    user_base_data["bio"] = "A" * 501  # Beyond max length
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Test missing optional fields
def test_user_base_missing_optional_fields(user_base_data):
    optional_fields = ["nickname", "first_name", "last_name", "bio", "profile_picture_url"]
    for field in optional_fields:
        user_base_data.pop(field, None)  # Remove optional field
    user = UserBase(**user_base_data)
    for field in optional_fields:
        assert getattr(user, field) is None  # Ensure default is None

# Test invalid data types for fields
@pytest.mark.parametrize("field, value", [
    ("nickname", 123),  # Invalid type for nickname
    ("email", ["not", "an", "email"]),  # Invalid type for email
    ("bio", {"invalid": "type"})  # Invalid type for bio
])
def test_user_base_invalid_field_types(field, value, user_base_data):
    user_base_data[field] = value
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Test invalid email addresses
@pytest.mark.parametrize("email", ["plainaddress", "@missingusername.com", "user@.missingdomain"])
def test_user_base_invalid_email_addresses(email, user_base_data):
    user_base_data["email"] = email
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Test valid and invalid LinkedIn URLs
@pytest.mark.parametrize("url", ["https://linkedin.com/in/validuser", None])
def test_user_base_valid_linkedin_url(url, user_base_data):
    user_base_data["linkedin_profile_url"] = url
    user = UserBase(**user_base_data)
    assert user.linkedin_profile_url == url

@pytest.mark.parametrize("url", ["ftp://invalid.com", "http:/missing-slash.com", "not-a-url"])
def test_user_base_invalid_linkedin_url(url, user_base_data):
    user_base_data["linkedin_profile_url"] = url
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Ensure missing optional fields do not raise errors
def test_user_base_no_optional_fields(user_base_data):
    user = UserBase(email=user_base_data["email"])
    assert user.nickname is None
    assert user.bio is None
