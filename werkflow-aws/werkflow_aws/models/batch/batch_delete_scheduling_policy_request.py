from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchDeleteSchedulingPolicyRequest(BaseModel):
    arn: StrictStr
