import uuid


def generate_unique_id():
    unique_id = uuid.uuid4()
    return str(unique_id)
