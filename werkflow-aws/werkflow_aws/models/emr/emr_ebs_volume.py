from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMREbsVolume(BaseModel):
    Device: StrictStr | None = None
    VolumeId: StrictStr | None = None
