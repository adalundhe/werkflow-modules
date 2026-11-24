from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_ecs_task_definition_container_definitions_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsDetails
from .security_hub_aws_ecs_task_definition_inference_accelerators_details import SecurityHubAwsEcsTaskDefinitionInferenceAcceleratorsDetails
from .security_hub_aws_ecs_task_definition_placement_constraints_details import SecurityHubAwsEcsTaskDefinitionPlacementConstraintsDetails
from .security_hub_aws_ecs_task_definition_proxy_configuration_details import SecurityHubAwsEcsTaskDefinitionProxyConfigurationDetails
from .security_hub_aws_ecs_task_definition_volumes_details import SecurityHubAwsEcsTaskDefinitionVolumesDetails


class SecurityHubAwsEcsTaskDefinitionDetails(BaseModel):
    ContainerDefinitions: list[SecurityHubAwsEcsTaskDefinitionContainerDefinitionsDetails] | None = None
    Cpu: StrictStr | None = None
    ExecutionRoleArn: StrictStr | None = None
    Family: StrictStr | None = None
    InferenceAccelerators: list[SecurityHubAwsEcsTaskDefinitionInferenceAcceleratorsDetails] | None = None
    IpcMode: StrictStr | None = None
    Memory: StrictStr | None = None
    NetworkMode: StrictStr | None = None
    PidMode: StrictStr | None = None
    PlacementConstraints: list[SecurityHubAwsEcsTaskDefinitionPlacementConstraintsDetails] | None = None
    ProxyConfiguration: SecurityHubAwsEcsTaskDefinitionProxyConfigurationDetails | None = None
    RequiresCompatibilities: list[StrictStr] | None = None
    TaskRoleArn: StrictStr | None = None
    Volumes: list[SecurityHubAwsEcsTaskDefinitionVolumesDetails] | None = None
    Status: StrictStr | None = None
