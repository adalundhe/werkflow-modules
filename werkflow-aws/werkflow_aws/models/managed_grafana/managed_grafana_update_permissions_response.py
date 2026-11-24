from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .managed_grafana_update_error import ManagedGrafanaUpdateError


class ManagedGrafanaUpdatePermissionsResponse(BaseModel):
    errors: list[ManagedGrafanaUpdateError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
