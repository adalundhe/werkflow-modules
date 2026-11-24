from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .managed_grafana_authentication_description import ManagedGrafanaAuthenticationDescription


class ManagedGrafanaUpdateWorkspaceAuthenticationResponse(BaseModel):
    authentication: ManagedGrafanaAuthenticationDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
