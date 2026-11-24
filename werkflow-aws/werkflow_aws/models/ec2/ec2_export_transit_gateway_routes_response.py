from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EC2ExportTransitGatewayRoutesResponse(BaseModel):
    S3Location: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
