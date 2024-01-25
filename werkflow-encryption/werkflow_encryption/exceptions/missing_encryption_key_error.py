class MissingEncryptionKeyError(Exception):

    def __init__(self):
        super().__init__(
            'No encryption key found.\nBe sure to set the key to the same one used to encrypt the secret!'
        )