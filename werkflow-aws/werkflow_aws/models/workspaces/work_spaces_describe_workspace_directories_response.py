from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .work_spaces_workspace_directory import WorkSpacesWorkspaceDirectory


class WorkSpacesDescribeWorkspaceDirectoriesResponse(BaseModel):
    Directories: list[WorkSpacesWorkspaceDirectory] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
