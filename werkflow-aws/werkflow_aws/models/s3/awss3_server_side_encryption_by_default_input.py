from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AWSS3ServerSideEncryptionByDefaultInput(BaseModel):
    SSEAlgorithm: Literal['AES256', 'aws:fsx', 'aws:backup', 'aws:kms', 'aws:kms:dsse']
    KMSMasterKeyID: StrictStr | None = None
