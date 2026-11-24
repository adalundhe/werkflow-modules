from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_policy_status import AWSS3PolicyStatus


class AWSS3GetBucketPolicyStatusResponse(BaseModel):
    PolicyStatus: AWSS3PolicyStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
