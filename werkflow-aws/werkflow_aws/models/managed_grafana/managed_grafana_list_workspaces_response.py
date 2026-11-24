from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .managed_grafana_workspace_summary import ManagedGrafanaWorkspaceSummary


class ManagedGrafanaListWorkspacesResponse(BaseModel):
    workspaces: list[ManagedGrafanaWorkspaceSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
