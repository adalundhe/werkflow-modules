from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_trail_resource_tag import CloudTrailResourceTag


class CloudTrailListTagsResponse(BaseModel):
    ResourceTagList: list[CloudTrailResourceTag] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
