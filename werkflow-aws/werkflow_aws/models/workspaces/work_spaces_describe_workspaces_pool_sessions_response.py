from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .workspaces_pool_session import WorkspacesPoolSession


class WorkSpacesDescribeWorkspacesPoolSessionsResponse(BaseModel):
    Sessions: list[WorkspacesPoolSession] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
