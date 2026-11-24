from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_object_lock_legal_hold import AWSS3ObjectLockLegalHold


class AWSS3GetObjectLegalHoldResponse(BaseModel):
    LegalHold: AWSS3ObjectLockLegalHold | None = None
    ResponseMetadata: dict[str, Any] | None = None
