from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_volume_mount import SecurityHubVolumeMount


class SecurityHubContainerDetails(BaseModel):
    ContainerRuntime: StrictStr | None = None
    Name: StrictStr | None = None
    ImageId: StrictStr | None = None
    ImageName: StrictStr | None = None
    LaunchedAt: StrictStr | None = None
    VolumeMounts: list[SecurityHubVolumeMount] | None = None
    Privileged: StrictBool | None = None
