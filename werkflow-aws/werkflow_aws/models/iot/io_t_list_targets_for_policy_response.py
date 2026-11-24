from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTListTargetsForPolicyResponse(BaseModel):
    targets: list[StrictStr] | None = None
    nextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
