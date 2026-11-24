from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .eks_capacity_types import EKSCapacityTypes
from .eks_launch_template_specification import EKSLaunchTemplateSpecification
from .eks_node_repair_config import EKSNodeRepairConfig
from .eks_nodegroup_scaling_config import EKSNodegroupScalingConfig
from .eks_nodegroup_update_config import EKSNodegroupUpdateConfig
from .eks_remote_access_config import EKSRemoteAccessConfig
from .eks_taint import EKSTaint
from .eks_warm_pool_config import EKSWarmPoolConfig
from .eksami_types import EKSAMITypes


class EKSCreateNodegroupRequest(BaseModel):
    clusterName: StrictStr
    nodegroupName: StrictStr
    subnets: list[StrictStr]
    nodeRole: StrictStr
    scalingConfig: EKSNodegroupScalingConfig | None = None
    diskSize: StrictInt | None = None
    instanceTypes: list[StrictStr] | None = None
    amiType: EKSAMITypes | None = None
    remoteAccess: EKSRemoteAccessConfig | None = None
    labels: dict[StrictStr, StrictStr] | None = None
    taints: list[EKSTaint] | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    clientRequestToken: StrictStr | None = None
    launchTemplate: EKSLaunchTemplateSpecification | None = None
    updateConfig: EKSNodegroupUpdateConfig | None = None
    nodeRepairConfig: EKSNodeRepairConfig | None = None
    capacityType: EKSCapacityTypes | None = None
    version: StrictStr | None = None
    releaseVersion: StrictStr | None = None
    warmPoolConfig: EKSWarmPoolConfig | None = None
