from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .work_spaces_workspace import WorkSpacesWorkspace


class WorkSpacesDescribeWorkspacesResponse(BaseModel):
    Workspaces: list[WorkSpacesWorkspace] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
