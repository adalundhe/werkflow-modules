from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .eks_nodegroup_update_strategies import EKSNodegroupUpdateStrategies


class EKSNodegroupUpdateConfig(BaseModel):
    maxUnavailable: StrictInt | None = None
    maxUnavailablePercentage: StrictInt | None = None
    updateStrategy: EKSNodegroupUpdateStrategies | None = None
