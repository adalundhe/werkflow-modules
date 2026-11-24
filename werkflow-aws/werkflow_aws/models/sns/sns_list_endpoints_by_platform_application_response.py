from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sns_endpoint import SNSEndpoint


class SNSListEndpointsByPlatformApplicationResponse(BaseModel):
    Endpoints: list[SNSEndpoint] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
