from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dms_tag import DMSTag


class DMSAddTagsToResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: list[DMSTag]
