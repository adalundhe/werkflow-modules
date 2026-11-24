from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SSMPutResourcePolicyResponse(BaseModel):
    PolicyId: StrictStr | None = None
    PolicyHash: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
