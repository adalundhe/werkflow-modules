from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueCloudWatchEncryption(BaseModel):
    CloudWatchEncryptionMode: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
