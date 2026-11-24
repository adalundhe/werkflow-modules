from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_workspace_page import ConnectWorkspacePage


class ConnectListWorkspacePagesResponse(BaseModel):
    NextToken: StrictStr | None = None
    WorkspacePageList: list[ConnectWorkspacePage] | None = None
    ResponseMetadata: dict[str, Any] | None = None
