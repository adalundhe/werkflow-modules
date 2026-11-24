from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class EC2GetVerifiedAccessGroupPolicyResponse(BaseModel):
    PolicyEnabled: StrictBool | None = None
    PolicyDocument: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
