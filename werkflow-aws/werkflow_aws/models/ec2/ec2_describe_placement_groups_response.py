from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_placement_group import EC2PlacementGroup


class EC2DescribePlacementGroupsResponse(BaseModel):
    PlacementGroups: list[EC2PlacementGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None
