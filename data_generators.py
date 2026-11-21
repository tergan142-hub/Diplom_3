import uuid
from faker import Faker

fake = Faker("en_US")

def generate_name():
    return "".join(c for c in fake.first_name() if c.isalpha())

def generate_email():
    return f"{uuid.uuid4().hex[:10]}@example.com"

def generate_password(length=10):
    return fake.password(
        length=length,
        special_chars=False,
        digits=True,
        upper_case=True,
        lower_case=True,
    )

def generate_user_data():
    return {
        "name": generate_name(),
        "email": generate_email(),
        "password": generate_password(),
    }

def normalize_order_number(number: str) -> str:
    return number.strip().lstrip("0") or "0"