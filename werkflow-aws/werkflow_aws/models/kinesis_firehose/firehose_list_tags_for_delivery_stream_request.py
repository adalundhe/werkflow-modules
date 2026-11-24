from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FirehoseListTagsForDeliveryStreamRequest(BaseModel):
    DeliveryStreamName: StrictStr
    ExclusiveStartTagKey: StrictStr | None = None
    Limit: StrictInt | None = None
