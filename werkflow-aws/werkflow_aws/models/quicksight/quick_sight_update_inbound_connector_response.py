from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightUpdateInboundConnectorResponse(BaseModel):
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    InboundConnectorId: StrictStr | None = None
    Arn: StrictStr | None = None
    InboundConnectorStatus: StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
