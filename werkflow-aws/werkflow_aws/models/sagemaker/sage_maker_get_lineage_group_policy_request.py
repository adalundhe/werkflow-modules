from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerGetLineageGroupPolicyRequest(BaseModel):
    LineageGroupName: StrictStr
