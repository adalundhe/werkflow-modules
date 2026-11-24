from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .x_ray_group import XRayGroup


class XRayCreateGroupResponse(BaseModel):
    Group: XRayGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
