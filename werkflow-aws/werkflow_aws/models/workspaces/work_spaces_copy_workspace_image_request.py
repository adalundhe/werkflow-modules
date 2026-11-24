from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_tag import WorkSpacesTag


class WorkSpacesCopyWorkspaceImageRequest(BaseModel):
    Name: StrictStr
    SourceImageId: StrictStr
    SourceRegion: StrictStr
    Description: StrictStr | None = None
    Tags: list[WorkSpacesTag] | None = None
