from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_authorizer_summary import IoTAuthorizerSummary


class IoTListAuthorizersResponse(BaseModel):
    authorizers: list[IoTAuthorizerSummary] | None = None
    nextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
