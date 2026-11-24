from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .x_ray_resource_policy import XRayResourcePolicy


class XRayPutResourcePolicyResponse(BaseModel):
    ResourcePolicy: XRayResourcePolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
