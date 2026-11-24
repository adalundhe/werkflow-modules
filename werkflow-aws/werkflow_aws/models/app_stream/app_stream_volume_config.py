from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AppStreamVolumeConfig(BaseModel):
    VolumeSizeInGb: StrictInt | None = None
