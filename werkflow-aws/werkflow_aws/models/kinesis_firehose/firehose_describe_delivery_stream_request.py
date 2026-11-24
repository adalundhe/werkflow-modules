from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FirehoseDescribeDeliveryStreamRequest(BaseModel):
    DeliveryStreamName: StrictStr
    Limit: StrictInt | None = None
    ExclusiveStartDestinationId: StrictStr | None = None
