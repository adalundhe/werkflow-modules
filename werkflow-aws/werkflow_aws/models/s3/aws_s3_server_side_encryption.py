from typing import Literal

AWSS3ServerSideEncryption = Literal[
    'AES256',
    'aws:kms',
    'aws:kms:dsse'
]