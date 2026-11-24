from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_trail_tag import CloudTrailTag


class CloudTrailRemoveTagsRequest(BaseModel):
    ResourceId: StrictStr
    TagsList: list[CloudTrailTag]
