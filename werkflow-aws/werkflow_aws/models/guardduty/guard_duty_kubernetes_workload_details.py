from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .guard_duty_container import GuardDutyContainer
from .guard_duty_volume import GuardDutyVolume


class GuardDutyKubernetesWorkloadDetails(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Uid: StrictStr | None = None
    Namespace: StrictStr | None = None
    HostNetwork: StrictBool | None = None
    ServiceAccountName: StrictStr | None = None
    Containers: list[GuardDutyContainer] | None = None
    Volumes: list[GuardDutyVolume] | None = None
    HostIPC: StrictBool | None = None
    HostPID: StrictBool | None = None
