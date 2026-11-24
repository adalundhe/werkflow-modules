from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class StorageGatewayUpdateGatewayInformationRequest(BaseModel):
    GatewayARN: StrictStr
    GatewayName: StrictStr | None = None
    GatewayTimezone: StrictStr | None = None
    CloudWatchLogGroupARN: StrictStr | None = None
    GatewayCapacity: Literal['Small', 'Medium', 'Large'] | None = None
