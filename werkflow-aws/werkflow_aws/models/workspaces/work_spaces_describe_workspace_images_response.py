from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .work_spaces_workspace_image import WorkSpacesWorkspaceImage


class WorkSpacesDescribeWorkspaceImagesResponse(BaseModel):
    Images: list[WorkSpacesWorkspaceImage] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
