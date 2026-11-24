from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsPutDeliverySourceRequest(BaseModel):
    name: StrictStr
    resourceArn: StrictStr
    logType: StrictStr
    tags: dict[StrictStr, StrictStr] | None = None
    deliverySourceConfiguration: dict[StrictStr, StrictStr] | None = None
