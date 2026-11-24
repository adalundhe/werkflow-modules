from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_workspace_summary import ConnectWorkspaceSummary


class ConnectListWorkspacesResponse(BaseModel):
    NextToken: StrictStr | None = None
    WorkspaceSummaryList: list[ConnectWorkspaceSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
