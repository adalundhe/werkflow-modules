from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_tag import WorkSpacesTag


class WorkSpacesCreateTagsRequest(BaseModel):
    ResourceId: StrictStr
    Tags: list[WorkSpacesTag]
