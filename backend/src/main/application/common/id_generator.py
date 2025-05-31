import uuid

def generate_id(three_letter_domain: str) -> str:
    return f"{three_letter_domain}-{uuid.uuid4()}"