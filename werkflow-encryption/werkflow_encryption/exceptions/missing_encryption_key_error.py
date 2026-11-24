from typing import Optional


class MissingEncryptionKeyError(Exception):

    def __init__(self, message: Optional[str] = None) -> None:
        super().__init__(
            message
            or 'No encryption key found.\nBe sure to set the key to the same one used to encrypt the secret!'
        )
