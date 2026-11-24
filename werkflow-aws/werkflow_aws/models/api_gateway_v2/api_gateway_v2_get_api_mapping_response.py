from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetApiMappingResponse(BaseModel):
    ApiId: StrictStr | None = None
    ApiMappingId: StrictStr | None = None
    ApiMappingKey: StrictStr | None = None
    Stage: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
