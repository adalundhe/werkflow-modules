from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightCreateInboundConnectorResponse(BaseModel):
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    InboundConnectorId: StrictStr | None = None
    Arn: StrictStr | None = None
    TenantUrl: StrictStr | None = None
    InboundConnectorStatus: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
