from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .emr_instance_group import EMRInstanceGroup


class EMRListInstanceGroupsResponse(BaseModel):
    InstanceGroups: list[EMRInstanceGroup] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
