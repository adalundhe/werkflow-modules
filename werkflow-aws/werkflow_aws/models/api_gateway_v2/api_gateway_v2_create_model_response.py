from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class APIGatewayV2CreateModelResponse(BaseModel):
    ContentType: StrictStr | None = None
    Description: StrictStr | None = None
    ModelId: StrictStr | None = None
    Name: StrictStr | None = None
    Schema: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
