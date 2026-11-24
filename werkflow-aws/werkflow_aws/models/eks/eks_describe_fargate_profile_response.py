from __future__ import annotations
from pydantic import BaseModel
from .eks_fargate_profile import EKSFargateProfile


class EKSDescribeFargateProfileResponse(BaseModel):
    fargateProfile: EKSFargateProfile | None = None
