from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class BatchCreateSchedulingPolicyResponse(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
