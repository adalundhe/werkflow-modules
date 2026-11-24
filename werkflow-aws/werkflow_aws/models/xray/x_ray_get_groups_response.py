from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .x_ray_group_summary import XRayGroupSummary


class XRayGetGroupsResponse(BaseModel):
    Groups: list[XRayGroupSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
