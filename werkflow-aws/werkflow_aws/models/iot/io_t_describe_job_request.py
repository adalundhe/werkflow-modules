from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTDescribeJobRequest(BaseModel):
    jobId: StrictStr
    beforeSubstitution: StrictBool | None = None
