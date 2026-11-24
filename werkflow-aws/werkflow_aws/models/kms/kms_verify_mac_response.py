from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class KMSVerifyMacResponse(BaseModel):
    KeyId: StrictStr | None = None
    MacValid: StrictBool | None = None
    MacAlgorithm: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
