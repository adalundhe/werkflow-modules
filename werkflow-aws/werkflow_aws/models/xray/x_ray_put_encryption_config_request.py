from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class XRayPutEncryptionConfigRequest(BaseModel):
    Type: Literal['NONE', 'KMS']
    KeyId: StrictStr | None = None
