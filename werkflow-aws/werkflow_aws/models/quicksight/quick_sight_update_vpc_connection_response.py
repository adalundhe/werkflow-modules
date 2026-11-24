from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightUpdateVPCConnectionResponse(BaseModel):
    Arn: StrictStr | None = None
    VPCConnectionId: StrictStr | None = None
    UpdateStatus: StrictStr | None = None
    AvailabilityStatus: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
