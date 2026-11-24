from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .eks_capacity_types import EKSCapacityTypes
from .eks_launch_template_specification import EKSLaunchTemplateSpecification
from .eks_node_repair_config import EKSNodeRepairConfig
from .eks_nodegroup_health import EKSNodegroupHealth
from .eks_nodegroup_resources import EKSNodegroupResources
from .eks_nodegroup_scaling_config import EKSNodegroupScalingConfig
from .eks_nodegroup_status import EKSNodegroupStatus
from .eks_nodegroup_update_config import EKSNodegroupUpdateConfig
from .eks_remote_access_config import EKSRemoteAccessConfig
from .eks_taint import EKSTaint
from .eks_warm_pool_config import EKSWarmPoolConfig
from .eksami_types import EKSAMITypes


class EKSNodegroup(BaseModel):
    nodegroupName: StrictStr | None = None
    nodegroupArn: StrictStr | None = None
    clusterName: StrictStr | None = None
    version: StrictStr | None = None
    releaseVersion: StrictStr | None = None
    createdAt: datetime.datetime | None = None
    modifiedAt: datetime.datetime | None = None
    status: EKSNodegroupStatus | None = None
    capacityType: EKSCapacityTypes | None = None
    scalingConfig: EKSNodegroupScalingConfig | None = None
    instanceTypes: list[StrictStr] | None = None
    subnets: list[StrictStr] | None = None
    remoteAccess: EKSRemoteAccessConfig | None = None
    amiType: EKSAMITypes | None = None
    nodeRole: StrictStr | None = None
    labels: dict[StrictStr, StrictStr] | None = None
    taints: list[EKSTaint] | None = None
    resources: EKSNodegroupResources | None = None
    diskSize: StrictInt | None = None
    health: EKSNodegroupHealth | None = None
    updateConfig: EKSNodegroupUpdateConfig | None = None
    nodeRepairConfig: EKSNodeRepairConfig | None = None
    launchTemplate: EKSLaunchTemplateSpecification | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    warmPoolConfig: EKSWarmPoolConfig | None = None
