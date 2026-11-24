from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .eks_fargate_profile_health import EKSFargateProfileHealth
from .eks_fargate_profile_selector import EKSFargateProfileSelector
from .eks_fargate_profile_status import EKSFargateProfileStatus


class EKSFargateProfile(BaseModel):
    fargateProfileName: StrictStr | None = None
    fargateProfileArn: StrictStr | None = None
    clusterName: StrictStr | None = None
    createdAt: datetime.datetime | None = None
    podExecutionRoleArn: StrictStr | None = None
    subnets: list[StrictStr] | None = None
    selectors: list[EKSFargateProfileSelector] | None = None
    status: EKSFargateProfileStatus | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    health: EKSFargateProfileHealth | None = None
