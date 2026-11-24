from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class StorageGatewayJoinDomainResponse(BaseModel):
    GatewayARN: StrictStr | None = None
    ActiveDirectoryStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
