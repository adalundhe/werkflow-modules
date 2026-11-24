from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightUpdateActionConnectorResponse(BaseModel):
    Arn: StrictStr | None = None
    ActionConnectorId: StrictStr | None = None
    RequestId: StrictStr | None = None
    UpdateStatus: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
