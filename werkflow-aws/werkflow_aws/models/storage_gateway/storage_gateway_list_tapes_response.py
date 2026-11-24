from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .storage_gateway_tape_info import StorageGatewayTapeInfo


class StorageGatewayListTapesResponse(BaseModel):
    TapeInfos: list[StorageGatewayTapeInfo] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
