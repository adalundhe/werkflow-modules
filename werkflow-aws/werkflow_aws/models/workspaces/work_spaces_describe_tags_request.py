from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesDescribeTagsRequest(BaseModel):
    ResourceId: StrictStr
