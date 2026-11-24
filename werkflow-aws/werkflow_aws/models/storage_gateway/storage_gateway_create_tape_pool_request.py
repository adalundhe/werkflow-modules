from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .storage_gateway_tag import StorageGatewayTag


class StorageGatewayCreateTapePoolRequest(BaseModel):
    PoolName: StrictStr
    StorageClass: Literal['DEEP_ARCHIVE', 'GLACIER']
    RetentionLockType: Literal['COMPLIANCE', 'GOVERNANCE', 'NONE'] | None = None
    RetentionLockTimeInDays: StrictInt | None = None
    Tags: list[StorageGatewayTag] | None = None
