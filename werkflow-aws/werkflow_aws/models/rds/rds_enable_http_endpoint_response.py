from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class RDSEnableHttpEndpointResponse(BaseModel):
    ResourceArn: StrictStr | None = None
    HttpEndpointEnabled: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
