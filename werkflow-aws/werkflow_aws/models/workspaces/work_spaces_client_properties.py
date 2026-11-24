from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesClientProperties(BaseModel):
    ReconnectEnabled: StrictStr | None = None
    LogUploadEnabled: StrictStr | None = None
    ClientExperiencePolicy: StrictStr | None = None
