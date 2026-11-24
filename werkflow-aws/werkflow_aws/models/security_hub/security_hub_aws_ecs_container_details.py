from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_aws_mount_point import SecurityHubAwsMountPoint


class SecurityHubAwsEcsContainerDetails(BaseModel):
    Name: StrictStr | None = None
    Image: StrictStr | None = None
    MountPoints: list[SecurityHubAwsMountPoint] | None = None
    Privileged: StrictBool | None = None
