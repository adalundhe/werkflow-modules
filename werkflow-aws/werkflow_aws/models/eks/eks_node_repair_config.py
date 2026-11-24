from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .eks_node_repair_config_overrides import EKSNodeRepairConfigOverrides


class EKSNodeRepairConfig(BaseModel):
    enabled: StrictBool | None = None
    maxUnhealthyNodeThresholdCount: StrictInt | None = None
    maxUnhealthyNodeThresholdPercentage: StrictInt | None = None
    maxParallelNodesRepairedCount: StrictInt | None = None
    maxParallelNodesRepairedPercentage: StrictInt | None = None
    nodeRepairConfigOverrides: list[EKSNodeRepairConfigOverrides] | None = None
