from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class StorageGatewayUpdateGatewayInformationResponse(BaseModel):
    GatewayARN: StrictStr | None = None
    GatewayName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
