from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedGrafanaRoleValues(BaseModel):
    editor: list[StrictStr] | None = None
    admin: list[StrictStr] | None = None
