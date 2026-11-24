from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesDescribeWorkspaceSnapshotsRequest(BaseModel):
    WorkspaceId: StrictStr
