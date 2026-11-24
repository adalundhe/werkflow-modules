from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_deployment_configuration import SageMakerDeploymentConfiguration
from .sage_maker_update_cluster_software_instance_group_specification import SageMakerUpdateClusterSoftwareInstanceGroupSpecification


class SageMakerUpdateClusterSoftwareRequest(BaseModel):
    ClusterName: StrictStr
    InstanceGroups: list[SageMakerUpdateClusterSoftwareInstanceGroupSpecification] | None = None
    DeploymentConfig: SageMakerDeploymentConfiguration | None = None
    ImageId: StrictStr | None = None
