from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class StorageGatewayCreateTapesResponse(BaseModel):
    TapeARNs: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
