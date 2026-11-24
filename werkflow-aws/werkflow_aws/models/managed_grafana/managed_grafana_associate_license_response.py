from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .managed_grafana_workspace_description import ManagedGrafanaWorkspaceDescription


class ManagedGrafanaAssociateLicenseResponse(BaseModel):
    workspace: ManagedGrafanaWorkspaceDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
