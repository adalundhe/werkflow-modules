from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_cluster_metadata import SageMakerClusterMetadata
from .sage_maker_database_configuration_metadata import SageMakerDatabaseConfigurationMetadata
from .sage_maker_instance_group_metadata import SageMakerInstanceGroupMetadata
from .sage_maker_instance_group_scaling_metadata import SageMakerInstanceGroupScalingMetadata
from .sage_maker_instance_metadata import SageMakerInstanceMetadata
from .sage_maker_slurm_health_metadata import SageMakerSlurmHealthMetadata


class SageMakerEventMetadata(BaseModel):
    Cluster: SageMakerClusterMetadata | None = None
    InstanceGroup: SageMakerInstanceGroupMetadata | None = None
    InstanceGroupScaling: SageMakerInstanceGroupScalingMetadata | None = None
    Instance: SageMakerInstanceMetadata | None = None
    DatabaseConfiguration: SageMakerDatabaseConfigurationMetadata | None = None
    SlurmHealth: SageMakerSlurmHealthMetadata | None = None
