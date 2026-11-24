from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .storage_gateway_tape import StorageGatewayTape


class StorageGatewayDescribeTapesResponse(BaseModel):
    Tapes: list[StorageGatewayTape] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
