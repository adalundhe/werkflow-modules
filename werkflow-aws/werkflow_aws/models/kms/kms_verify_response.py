from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class KMSVerifyResponse(BaseModel):
    KeyId: StrictStr | None = None
    SignatureValid: StrictBool | None = None
    SigningAlgorithm: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
