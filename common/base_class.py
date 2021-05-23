from string import ascii_lowercase, digits, punctuation


class BaseCipher:
    """Base parent class for inheritance other implementations"""
    num_alphabet_type_map = {
        0: 'All',
        1: 'Letters',
        2: 'Letters and digits',
        3: 'Letters and punctuations'
    }

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

    def encrypt(self, message: str, **kwargs):
        """Must be redefined"""
        raise NotImplementedError

    def decrypt(self, message: str, **kwargs):
        """Must be redefined"""
        raise NotImplementedError
