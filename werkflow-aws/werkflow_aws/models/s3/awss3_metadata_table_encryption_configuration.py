from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AWSS3MetadataTableEncryptionConfiguration(BaseModel):
    SseAlgorithm: Literal['aws:kms', 'AES256']
    KmsKeyArn: StrictStr | None = None
