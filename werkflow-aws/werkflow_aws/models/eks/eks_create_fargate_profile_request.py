from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_fargate_profile_selector import EKSFargateProfileSelector


class EKSCreateFargateProfileRequest(BaseModel):
    fargateProfileName: StrictStr
    clusterName: StrictStr
    podExecutionRoleArn: StrictStr
    subnets: list[StrictStr] | None = None
    selectors: list[EKSFargateProfileSelector] | None = None
    clientRequestToken: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
