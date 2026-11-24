from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeLineageGroupRequest(BaseModel):
    LineageGroupName: StrictStr
