import re

def normalize_phone(phone_number: str) -> str:
    phone = re.sub(r"[^\d+]", "", phone_number)

    if phone.startswith("+"):
        return phone

    if phone.startswith("380"):
        return "+" + phone

    return "+38" + phone

phones = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

for phone in phones:
    print(f"Правильный номер: {normalize_phone(phone)}")
