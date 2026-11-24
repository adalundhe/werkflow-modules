from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ECSDiscoverPollEndpointResponse(BaseModel):
    endpoint: StrictStr | None = None
    telemetryEndpoint: StrictStr | None = None
    serviceConnectEndpoint: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
