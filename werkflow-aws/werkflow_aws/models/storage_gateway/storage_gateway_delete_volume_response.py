from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class StorageGatewayDeleteVolumeResponse(BaseModel):
    VolumeARN: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
