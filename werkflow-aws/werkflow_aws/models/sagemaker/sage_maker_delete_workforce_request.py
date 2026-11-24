from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteWorkforceRequest(BaseModel):
    WorkforceName: StrictStr
