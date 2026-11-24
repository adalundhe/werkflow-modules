from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayEncryptionConfig(BaseModel):
    KeyId: StrictStr | None = None
    Status: StrictStr | None = None
    Type: StrictStr | None = None
