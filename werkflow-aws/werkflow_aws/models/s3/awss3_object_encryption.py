from __future__ import annotations
from pydantic import BaseModel
from .awss3_ssekms_encryption import AWSS3SSEKMSEncryption


class AWSS3ObjectEncryption(BaseModel):
    SSEKMS: AWSS3SSEKMSEncryption | None = None
