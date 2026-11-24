from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .sage_maker_cluster_auto_scaling_config import SageMakerClusterAutoScalingConfig
from .sage_maker_cluster_instance_group_specification import SageMakerClusterInstanceGroupSpecification
from .sage_maker_cluster_orchestrator import SageMakerClusterOrchestrator
from .sage_maker_cluster_restricted_instance_group_specification import SageMakerClusterRestrictedInstanceGroupSpecification
from .sage_maker_cluster_restricted_instance_groups_config import SageMakerClusterRestrictedInstanceGroupsConfig
from .sage_maker_cluster_tiered_storage_config import SageMakerClusterTieredStorageConfig
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_vpc_config_model import SageMakerVpcConfigModel


class SageMakerCreateClusterRequest(BaseModel):
    ClusterName: StrictStr
    InstanceGroups: list[SageMakerClusterInstanceGroupSpecification] | None = None
    RestrictedInstanceGroups: list[SageMakerClusterRestrictedInstanceGroupSpecification] | None = None
    RestrictedInstanceGroupsConfig: SageMakerClusterRestrictedInstanceGroupsConfig | None = None
    VpcConfig: SageMakerVpcConfigModel | None = None
    Tags: list[SageMakerTagModel] | None = None
    Orchestrator: SageMakerClusterOrchestrator | None = None
    NodeRecovery: Literal['Automatic', 'None'] | None = None
    TieredStorageConfig: SageMakerClusterTieredStorageConfig | None = None
    NodeProvisioningMode: Literal['Continuous'] | None = None
    ClusterRole: StrictStr | None = None
    AutoScaling: SageMakerClusterAutoScalingConfig | None = None
