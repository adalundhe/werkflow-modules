from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSDescribeFargateProfileRequest(BaseModel):
    clusterName: StrictStr
    fargateProfileName: StrictStr
