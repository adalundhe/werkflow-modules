from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ComprehendCreateEndpointResponse(BaseModel):
    EndpointArn: StrictStr | None = None
    ModelArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
