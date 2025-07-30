from typing import Literal


AthenaEncryptionOption = Literal[
    'SSE_S3',
    'SSE_KMS',
    'CSE_KMS',
]