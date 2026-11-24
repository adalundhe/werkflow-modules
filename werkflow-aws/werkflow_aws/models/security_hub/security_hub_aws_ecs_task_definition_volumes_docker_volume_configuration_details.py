from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails(BaseModel):
    Autoprovision: StrictBool | None = None
    Driver: StrictStr | None = None
    DriverOpts: dict[StrictStr, StrictStr] | None = None
    Labels: dict[StrictStr, StrictStr] | None = None
    Scope: StrictStr | None = None
