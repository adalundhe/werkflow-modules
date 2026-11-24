from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDataQualityEncryption(BaseModel):
    DataQualityEncryptionMode: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
