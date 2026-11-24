from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class NetworkManagerUpdateNetworkResourceMetadataResponse(BaseModel):
    ResourceArn: StrictStr | None = None
    Metadata: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
