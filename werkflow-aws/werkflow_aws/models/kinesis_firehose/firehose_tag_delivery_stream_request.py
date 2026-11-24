from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .firehose_tag import FirehoseTag


class FirehoseTagDeliveryStreamRequest(BaseModel):
    DeliveryStreamName: StrictStr
    Tags: list[FirehoseTag]
