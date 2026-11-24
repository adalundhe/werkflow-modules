from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubVolumeMount(BaseModel):
    Name: StrictStr | None = None
    MountPath: StrictStr | None = None
