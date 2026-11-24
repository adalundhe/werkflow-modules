from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeModelPackageGroupRequest(BaseModel):
    ModelPackageGroupName: StrictStr
