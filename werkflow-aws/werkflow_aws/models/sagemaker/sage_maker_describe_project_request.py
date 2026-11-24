from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeProjectRequest(BaseModel):
    ProjectName: StrictStr
