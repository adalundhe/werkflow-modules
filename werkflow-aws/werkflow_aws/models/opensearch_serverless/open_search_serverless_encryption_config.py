from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchServerlessEncryptionConfig(BaseModel):
    aWSOwnedKey: StrictBool | None = None
    kmsKeyArn: StrictStr | None = None
