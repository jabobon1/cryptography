import secrets
from typing import Optional

from common.base_class import BaseCipher


class SubstitutionCipher(BaseCipher):
    """
    a substitution cipher is a method of encrypting in which units
    of plaintext are replaced with the ciphertext, in a defined manner
    """

    def __init__(self, alphabet_id: Optional[int] = 0):
        self.alphabet = self.get_alphabet(alphabet_id)
        self.letters_to_secret_map = self.random_encrypt_key(self.alphabet)
        self.secret_to_letters_map = {v: k for k, v in self.letters_to_secret_map.items()}

    @staticmethod
    def random_encrypt_key(alphabet: str):
        """Generates random char to char map    """
        l_alphabet = list(alphabet)
        alphabet_mapping = {}
        ind = 0
        while len(l_alphabet) > 0 and ind < len(alphabet):
            secret_char = secrets.choice(l_alphabet)
            alphabet_mapping[alphabet[ind]] = secret_char
            l_alphabet.remove(secret_char)
            ind += 1
        return alphabet_mapping

    def encrypt(self, message: str, letters_to_secret_map: Optional[dict] = None):
        message = message.lower()
        letters_to_secret_map = letters_to_secret_map or self.letters_to_secret_map
        encrypted_text = []
        for ch in message:
            encrypted_text.append(letters_to_secret_map.get(ch, ch))
        return ''.join(encrypted_text)

    def decrypt(self, message: str, secret_to_letters_map: Optional[dict] = None):
        message = message.lower()
        secret_to_letters_map = secret_to_letters_map or self.secret_to_letters_map
        decrypted_text = []
        for ch in message:
            decrypted_text.append(secret_to_letters_map.get(ch, ch))
        return ''.join(decrypted_text)


if __name__ == '__main__':
    plain_text = 'Hello, friend!'
    print(f'Message: {plain_text}')
    offset = 4
    cipherator = SubstitutionCipher(alphabet_id=0)
    encrypted_text = cipherator.encrypt(plain_text)
    print(f'Message encrypted: {encrypted_text}')
    decrypted_text = cipherator.decrypt(encrypted_text)
    print(f'Message decrypted: {decrypted_text}')
