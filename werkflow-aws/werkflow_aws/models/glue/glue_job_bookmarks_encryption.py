from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueJobBookmarksEncryption(BaseModel):
    JobBookmarksEncryptionMode: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
