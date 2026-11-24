from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseUntagDeliveryStreamRequest(BaseModel):
    DeliveryStreamName: StrictStr
    TagKeys: list[StrictStr]
