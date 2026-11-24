from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseStopDeliveryStreamEncryptionRequest(BaseModel):
    DeliveryStreamName: StrictStr
