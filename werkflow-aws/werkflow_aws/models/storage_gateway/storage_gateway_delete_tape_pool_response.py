from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class StorageGatewayDeleteTapePoolResponse(BaseModel):
    PoolARN: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
