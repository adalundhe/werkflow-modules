from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fms_policy import FMSPolicy


class FMSPutPolicyResponse(BaseModel):
    Policy: FMSPolicy | None = None
    PolicyArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
