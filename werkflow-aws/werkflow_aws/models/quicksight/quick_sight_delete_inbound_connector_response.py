from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightDeleteInboundConnectorResponse(BaseModel):
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    InboundConnectorId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
