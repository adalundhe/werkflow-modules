from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_trail_trail import CloudTrailTrail


class CloudTrailDescribeTrailsResponse(BaseModel):
    trailList: list[CloudTrailTrail] | None = None
    ResponseMetadata: dict[str, Any] | None = None
