from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_cluster_auto_scaling_config_output import SageMakerClusterAutoScalingConfigOutput
from .sage_maker_cluster_instance_group_details import SageMakerClusterInstanceGroupDetails
from .sage_maker_cluster_orchestrator import SageMakerClusterOrchestrator
from .sage_maker_cluster_restricted_instance_group_details import SageMakerClusterRestrictedInstanceGroupDetails
from .sage_maker_cluster_restricted_instance_groups_config_output import SageMakerClusterRestrictedInstanceGroupsConfigOutput
from .sage_maker_cluster_tiered_storage_config import SageMakerClusterTieredStorageConfig
from .sage_maker_vpc_config_model import SageMakerVpcConfigModel


class SageMakerDescribeClusterResponse(BaseModel):
    ClusterArn: StrictStr | None = None
    ClusterName: StrictStr | None = None
    ClusterStatus: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    FailureMessage: StrictStr | None = None
    InstanceGroups: list[SageMakerClusterInstanceGroupDetails] | None = None
    RestrictedInstanceGroups: list[SageMakerClusterRestrictedInstanceGroupDetails] | None = None
    RestrictedInstanceGroupsConfig: SageMakerClusterRestrictedInstanceGroupsConfigOutput | None = None
    VpcConfig: SageMakerVpcConfigModel | None = None
    Orchestrator: SageMakerClusterOrchestrator | None = None
    TieredStorageConfig: SageMakerClusterTieredStorageConfig | None = None
    NodeRecovery: StrictStr | None = None
    NodeProvisioningMode: StrictStr | None = None
    ClusterRole: StrictStr | None = None
    AutoScaling: SageMakerClusterAutoScalingConfigOutput | None = None
    ResponseMetadata: dict[str, Any] | None = None
