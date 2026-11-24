from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class StorageGatewayDeleteFileShareResponse(BaseModel):
    FileShareARN: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
