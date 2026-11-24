from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueS3Encryption(BaseModel):
    S3EncryptionMode: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
