from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .f_sx_volume import FSxVolume


class FSxDescribeVolumesResponse(BaseModel):
    Volumes: list[FSxVolume] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
