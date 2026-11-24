from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .auto_scaling_tag_description import AutoScalingTagDescription


class AutoScalingDescribeTagsResponse(BaseModel):
    Tags: list[AutoScalingTagDescription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
