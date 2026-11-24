from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .firehose_record import FirehoseRecord


class FirehosePutRecordBatchRequest(BaseModel):
    DeliveryStreamName: StrictStr
    Records: list[FirehoseRecord]
