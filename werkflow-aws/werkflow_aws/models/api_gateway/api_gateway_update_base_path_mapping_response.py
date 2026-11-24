from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class APIGatewayUpdateBasePathMappingResponse(BaseModel):
    basePath: StrictStr | None = None
    restApiId: StrictStr | None = None
    stage: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
