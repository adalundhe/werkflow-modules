from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteModelPackageGroupPolicyRequest(BaseModel):
    ModelPackageGroupName: StrictStr
