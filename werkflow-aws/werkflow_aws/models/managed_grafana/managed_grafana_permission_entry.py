from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .managed_grafana_user import ManagedGrafanaUser


class ManagedGrafanaPermissionEntry(BaseModel):
    user: ManagedGrafanaUser | None = None
    role: StrictStr | None = None
