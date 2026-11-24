from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class KMSGetKeyPolicyResponse(BaseModel):
    Policy: StrictStr | None = None
    PolicyName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
