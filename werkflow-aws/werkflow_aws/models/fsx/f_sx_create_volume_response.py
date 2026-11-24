from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .f_sx_volume import FSxVolume


class FSxCreateVolumeResponse(BaseModel):
    Volume: FSxVolume | None = None
    ResponseMetadata: dict[str, Any] | None = None
