import base64

def encode_name(name: str) -> str:
    """Encode a name to Base64 format.

    Args:
        name (str): The name to encode.

    Returns:
        str: Base64 encoded name.
    """
    return base64.b64encode(name.encode()).decode()
