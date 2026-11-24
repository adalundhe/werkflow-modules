from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_placement_group import EC2PlacementGroup


class EC2CreatePlacementGroupResponse(BaseModel):
    PlacementGroup: EC2PlacementGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
