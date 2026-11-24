from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_trail_tag import CloudTrailTag


class CloudTrailResourceTag(BaseModel):
    ResourceId: StrictStr | None = None
    TagsList: list[CloudTrailTag] | None = None
