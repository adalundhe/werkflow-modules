from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .x_ray_resource_policy import XRayResourcePolicy


class XRayListResourcePoliciesResponse(BaseModel):
    ResourcePolicies: list[XRayResourcePolicy] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
