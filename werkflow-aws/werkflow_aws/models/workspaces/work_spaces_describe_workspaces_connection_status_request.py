from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesDescribeWorkspacesConnectionStatusRequest(BaseModel):
    WorkspaceIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
