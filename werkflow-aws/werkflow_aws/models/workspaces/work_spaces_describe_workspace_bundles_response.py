from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .work_spaces_workspace_bundle import WorkSpacesWorkspaceBundle


class WorkSpacesDescribeWorkspaceBundlesResponse(BaseModel):
    Bundles: list[WorkSpacesWorkspaceBundle] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
