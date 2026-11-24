from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeWorkforceRequest(BaseModel):
    WorkforceName: StrictStr
