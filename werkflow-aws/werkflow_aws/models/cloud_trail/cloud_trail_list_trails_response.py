from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_trail_trail_info import CloudTrailTrailInfo


class CloudTrailListTrailsResponse(BaseModel):
    Trails: list[CloudTrailTrailInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
