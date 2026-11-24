from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_data_table_lock_version import ConnectDataTableLockVersion


class ConnectCreateDataTableAttributeResponse(BaseModel):
    Name: StrictStr | None = None
    AttributeId: StrictStr | None = None
    LockVersion: ConnectDataTableLockVersion | None = None
    ResponseMetadata: dict[str, Any] | None = None
