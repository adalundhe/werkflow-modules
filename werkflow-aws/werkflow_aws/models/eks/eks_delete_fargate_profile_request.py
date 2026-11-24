from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSDeleteFargateProfileRequest(BaseModel):
    clusterName: StrictStr
    fargateProfileName: StrictStr
