from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_policy import IoTPolicy


class IoTListPoliciesResponse(BaseModel):
    policies: list[IoTPolicy] | None = None
    nextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
