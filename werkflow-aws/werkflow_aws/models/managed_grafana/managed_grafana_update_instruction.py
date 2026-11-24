from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .managed_grafana_user import ManagedGrafanaUser


class ManagedGrafanaUpdateInstruction(BaseModel):
    action: StrictStr | None = None
    role: StrictStr | None = None
    users: list[ManagedGrafanaUser] | None = None
