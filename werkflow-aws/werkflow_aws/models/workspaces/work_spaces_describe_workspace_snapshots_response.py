from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .work_spaces_snapshot import WorkSpacesSnapshot


class WorkSpacesDescribeWorkspaceSnapshotsResponse(BaseModel):
    RebuildSnapshots: list[WorkSpacesSnapshot] | None = None
    RestoreSnapshots: list[WorkSpacesSnapshot] | None = None
    ResponseMetadata: dict[str, Any] | None = None
