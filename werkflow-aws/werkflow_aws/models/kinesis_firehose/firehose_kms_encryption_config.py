from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseKMSEncryptionConfig(BaseModel):
    AWSKMSKeyARN: StrictStr | None = None
