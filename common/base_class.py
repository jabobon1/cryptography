from typing import Optional, Union


class BaseCipher:
    """Base parent class for inheritance other implementations"""

    def __init__(self, salt: Optional[Union[str, int]] = None):
        self.salt = salt

    def encrypt(self, message: str):
        raise NotImplementedError

    def decrypt(self, message: str):
        raise NotImplementedError
