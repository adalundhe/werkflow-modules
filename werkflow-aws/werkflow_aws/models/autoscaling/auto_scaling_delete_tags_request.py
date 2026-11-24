from __future__ import annotations
from pydantic import BaseModel
from .auto_scaling_tag import AutoScalingTag


class AutoScalingDeleteTagsRequest(BaseModel):
    Tags: list[AutoScalingTag]
