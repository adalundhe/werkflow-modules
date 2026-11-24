from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FirehoseDeleteDeliveryStreamRequest(BaseModel):
    DeliveryStreamName: StrictStr
    AllowForceDelete: StrictBool | None = None
