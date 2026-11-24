from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class StorageGatewayRefreshCacheResponse(BaseModel):
    FileShareARN: StrictStr | None = None
    NotificationId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
