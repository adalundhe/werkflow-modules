from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_ecs_container_details import SecurityHubAwsEcsContainerDetails
from .security_hub_aws_ecs_task_volume_details import SecurityHubAwsEcsTaskVolumeDetails


class SecurityHubAwsEcsTaskDetails(BaseModel):
    ClusterArn: StrictStr | None = None
    TaskDefinitionArn: StrictStr | None = None
    Version: StrictStr | None = None
    CreatedAt: StrictStr | None = None
    StartedAt: StrictStr | None = None
    StartedBy: StrictStr | None = None
    Group: StrictStr | None = None
    Volumes: list[SecurityHubAwsEcsTaskVolumeDetails] | None = None
    Containers: list[SecurityHubAwsEcsContainerDetails] | None = None
