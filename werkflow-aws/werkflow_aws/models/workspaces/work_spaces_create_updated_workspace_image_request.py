from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_tag import WorkSpacesTag


class WorkSpacesCreateUpdatedWorkspaceImageRequest(BaseModel):
    Name: StrictStr
    Description: StrictStr
    SourceImageId: StrictStr
    Tags: list[WorkSpacesTag] | None = None
