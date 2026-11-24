from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieDescribeClassificationJobRequest(BaseModel):
    jobId: StrictStr
