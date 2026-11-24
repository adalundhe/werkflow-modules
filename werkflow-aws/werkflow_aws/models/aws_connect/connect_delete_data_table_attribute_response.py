from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_data_table_lock_version import ConnectDataTableLockVersion


class ConnectDeleteDataTableAttributeResponse(BaseModel):
    LockVersion: ConnectDataTableLockVersion | None = None
    ResponseMetadata: dict[str, Any] | None = None
