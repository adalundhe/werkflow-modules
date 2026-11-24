from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteModelPackageGroupRequest(BaseModel):
    ModelPackageGroupName: StrictStr
