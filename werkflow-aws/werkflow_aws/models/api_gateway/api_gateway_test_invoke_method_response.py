from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class APIGatewayTestInvokeMethodResponse(BaseModel):
    status: StrictInt | None = None
    body: StrictStr | None = None
    headers: dict[StrictStr, StrictStr] | None = None
    multiValueHeaders: dict[StrictStr, list[StrictStr]] | None = None
    log: StrictStr | None = None
    latency: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
