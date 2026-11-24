from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PermissionsKeysBean(BaseModel):
    permissions: list[StrictStr] | None = None
