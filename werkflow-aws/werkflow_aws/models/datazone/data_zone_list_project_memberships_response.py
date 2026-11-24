from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_project_member import DataZoneProjectMember


class DataZoneListProjectMembershipsResponse(BaseModel):
    members: list[DataZoneProjectMember] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
