from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .firehose_record import FirehoseRecord


class FirehosePutRecordRequest(BaseModel):
    DeliveryStreamName: StrictStr
    Record: FirehoseRecord
