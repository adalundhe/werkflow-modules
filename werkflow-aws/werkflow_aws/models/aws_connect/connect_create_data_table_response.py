from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_data_table_lock_version import ConnectDataTableLockVersion


class ConnectCreateDataTableResponse(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    LockVersion: ConnectDataTableLockVersion | None = None
    ResponseMetadata: dict[str, Any] | None = None
