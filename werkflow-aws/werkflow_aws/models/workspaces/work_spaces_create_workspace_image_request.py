from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_tag import WorkSpacesTag


class WorkSpacesCreateWorkspaceImageRequest(BaseModel):
    Name: StrictStr
    Description: StrictStr
    WorkspaceId: StrictStr
    Tags: list[WorkSpacesTag] | None = None
