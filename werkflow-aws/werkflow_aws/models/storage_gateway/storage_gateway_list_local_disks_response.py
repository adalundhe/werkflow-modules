from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .storage_gateway_disk import StorageGatewayDisk


class StorageGatewayListLocalDisksResponse(BaseModel):
    GatewayARN: StrictStr | None = None
    Disks: list[StorageGatewayDisk] | None = None
    ResponseMetadata: dict[str, Any] | None = None
