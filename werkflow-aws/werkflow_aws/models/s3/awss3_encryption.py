from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AWSS3Encryption(BaseModel):
    EncryptionType: Literal['AES256', 'aws:fsx', 'aws:backup', 'aws:kms', 'aws:kms:dsse']
    KMSKeyId: StrictStr | None = None
    KMSContext: StrictStr | None = None
