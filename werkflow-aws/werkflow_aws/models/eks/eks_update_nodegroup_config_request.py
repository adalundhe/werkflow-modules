from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_node_repair_config import EKSNodeRepairConfig
from .eks_nodegroup_scaling_config import EKSNodegroupScalingConfig
from .eks_nodegroup_update_config import EKSNodegroupUpdateConfig
from .eks_update_labels_payload import EKSUpdateLabelsPayload
from .eks_update_taints_payload import EKSUpdateTaintsPayload
from .eks_warm_pool_config import EKSWarmPoolConfig


class EKSUpdateNodegroupConfigRequest(BaseModel):
    clusterName: StrictStr
    nodegroupName: StrictStr
    labels: EKSUpdateLabelsPayload | None = None
    taints: EKSUpdateTaintsPayload | None = None
    scalingConfig: EKSNodegroupScalingConfig | None = None
    updateConfig: EKSNodegroupUpdateConfig | None = None
    nodeRepairConfig: EKSNodeRepairConfig | None = None
    warmPoolConfig: EKSWarmPoolConfig | None = None
    clientRequestToken: StrictStr | None = None
