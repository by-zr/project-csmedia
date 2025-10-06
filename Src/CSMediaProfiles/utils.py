import uuid

def get_slug_url():
    slug_url = str(uuid.uuid4())[:10].replace('-', '').lower()
    return slug_url