from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_security_context import GuardDutySecurityContext
from .guard_duty_volume_mount import GuardDutyVolumeMount


class GuardDutyContainer(BaseModel):
    ContainerRuntime: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Image: StrictStr | None = None
    ImagePrefix: StrictStr | None = None
    VolumeMounts: list[GuardDutyVolumeMount] | None = None
    SecurityContext: GuardDutySecurityContext | None = None
