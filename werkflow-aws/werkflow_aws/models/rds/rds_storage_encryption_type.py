from __future__ import annotations
from typing import Literal


RDSStorageEncryptionType = Literal[
    'none',
    'sse-kms',
    'sse-rds',
]
