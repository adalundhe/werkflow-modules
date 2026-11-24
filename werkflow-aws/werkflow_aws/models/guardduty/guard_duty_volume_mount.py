from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyVolumeMount(BaseModel):
    Name: StrictStr | None = None
    MountPath: StrictStr | None = None
