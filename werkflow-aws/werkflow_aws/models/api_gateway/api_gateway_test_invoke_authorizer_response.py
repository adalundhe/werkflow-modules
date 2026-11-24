from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class APIGatewayTestInvokeAuthorizerResponse(BaseModel):
    clientStatus: StrictInt | None = None
    log: StrictStr | None = None
    latency: StrictInt | None = None
    principalId: StrictStr | None = None
    policy: StrictStr | None = None
    authorization: dict[StrictStr, list[StrictStr]] | None = None
    claims: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
