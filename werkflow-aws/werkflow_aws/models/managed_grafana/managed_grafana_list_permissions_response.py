from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .managed_grafana_permission_entry import ManagedGrafanaPermissionEntry


class ManagedGrafanaListPermissionsResponse(BaseModel):
    nextToken: StrictStr | None = None
    permissions: list[ManagedGrafanaPermissionEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
