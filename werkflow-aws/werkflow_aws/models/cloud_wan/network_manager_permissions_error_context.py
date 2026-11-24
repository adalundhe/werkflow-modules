from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerPermissionsErrorContext(BaseModel):
    MissingPermission: StrictStr | None = None
