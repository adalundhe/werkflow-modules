from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_ecs_task_volume_host_details import SecurityHubAwsEcsTaskVolumeHostDetails


class SecurityHubAwsEcsTaskVolumeDetails(BaseModel):
    Name: StrictStr | None = None
    Host: SecurityHubAwsEcsTaskVolumeHostDetails | None = None
