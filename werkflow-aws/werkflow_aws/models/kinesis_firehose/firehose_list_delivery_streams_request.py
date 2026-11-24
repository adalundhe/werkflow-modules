from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class FirehoseListDeliveryStreamsRequest(BaseModel):
    Limit: StrictInt | None = None
    DeliveryStreamType: Literal['DirectPut', 'KinesisStreamAsSource', 'MSKAsSource', 'DatabaseAsSource'] | None = None
    ExclusiveStartDeliveryStreamName: StrictStr | None = None
