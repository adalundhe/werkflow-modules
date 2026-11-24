from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_auto_scaling_group import EKSAutoScalingGroup


class EKSNodegroupResources(BaseModel):
    autoScalingGroups: list[EKSAutoScalingGroup] | None = None
    remoteAccessSecurityGroup: StrictStr | None = None
