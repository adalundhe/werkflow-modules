from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class AWSS3GetBucketPolicyResponse(BaseModel):
    Policy: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
