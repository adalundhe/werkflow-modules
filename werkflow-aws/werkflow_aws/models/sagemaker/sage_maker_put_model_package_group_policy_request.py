from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerPutModelPackageGroupPolicyRequest(BaseModel):
    ModelPackageGroupName: StrictStr
    ResourcePolicy: StrictStr
