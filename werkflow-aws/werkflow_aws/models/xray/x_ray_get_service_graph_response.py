from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .x_ray_service import XRayService


class XRayGetServiceGraphResponse(BaseModel):
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Services: list[XRayService] | None = None
    ContainsOldGroupVersions: StrictBool | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
