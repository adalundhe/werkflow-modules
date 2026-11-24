from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsMountPoint(BaseModel):
    SourceVolume: StrictStr | None = None
    ContainerPath: StrictStr | None = None
