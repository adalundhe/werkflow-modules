from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewaySMBLocalGroups(BaseModel):
    GatewayAdmins: list[StrictStr] | None = None
