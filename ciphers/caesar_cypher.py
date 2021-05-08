from string import ascii_lowercase, digits, punctuation
from typing import Optional

from common.base_class import BaseCipher


class CeasarCipher(BaseCipher):
    num_alphabet_type_map = {
        0: 'All',
        1: 'Letters',
        2: 'Letters and digits',
        3: 'Letters and punctuations'
    }

    def __init__(self, offset: int, alphabet_id: Optional[int] = 0):
        self.offset = offset
        self.alphabet = self.get_alphabet(alphabet_id)
        self.index_char_map, self.char_index_map = self.get_index_char_mappings(self.alphabet)

    def get_allowed_alphabet_types(self):
        return self.num_alphabet_type_map

    @staticmethod
    def get_index_char_mappings(alphabet: str) -> tuple[dict[int:str], dict[str:int]]:
        index_char_map: dict[int:str] = {}
        char_index_map: dict[str:int] = {}

        for ind, char in enumerate(alphabet):
            index_char_map[ind] = char
            char_index_map[char] = ind

        return index_char_map, char_index_map

    @staticmethod
    def get_alphabet(alphabet_id: int) -> str:
        if alphabet_id == 0:
            return ascii_lowercase + digits + punctuation
        elif alphabet_id == 1:
            return ascii_lowercase
        elif alphabet_id == 2:
            return ascii_lowercase + digits
        elif alphabet_id == 3:
            return ascii_lowercase + punctuation
        else:
            return ascii_lowercase + digits + punctuation

    def encrypt(self, message: str, offset: Optional[int] = None) -> str:
        """Encrypts the message with ceasar cipher"""
        offset = offset or self.offset
        message = message.lower()
        encrypted_message = []
        for symbol in message:
            char_index = self.char_index_map.get(symbol)
            if char_index is not None:
                char = self.index_char_map[(char_index + offset) % len(self.alphabet)]
                encrypted_message.append(char)
            else:
                encrypted_message.append(' ')
        return ''.join(encrypted_message)

    def decrypt(self, message: str, offset: Optional[int] = None):
        """Decrypts the message encrypted by ceasar cipher"""
        offset = offset or self.offset
        return self.encrypt(message, offset * -1)


if __name__ == '__main__':
    plain_text = 'Hello, friend!'
    print(f'Message: {plain_text}')
    offset = 4
    cipherator = CeasarCipher(offset=offset, alphabet_id=0)
    encrypted_text = cipherator.encrypt(plain_text)
    print(f'Message encrypted: {encrypted_text}')
    decrypted_text = cipherator.decrypt(encrypted_text)
    print(f'Message decrypted: {decrypted_text}')
