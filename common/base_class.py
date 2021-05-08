from typing import Optional, Union


class BaseCipher:
    """Base parent class for inheritance other implementations"""


    def encrypt(self, message: str, **kwargs):
        """Must be redefined"""
        raise NotImplementedError

    def decrypt(self, message: str, **kwargs):
        """Must be redefined"""
        raise NotImplementedError
