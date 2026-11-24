from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt
from .firehose_put_record_batch_response_entry import FirehosePutRecordBatchResponseEntry


class FirehosePutRecordBatchResponse(BaseModel):
    FailedPutCount: StrictInt | None = None
    Encrypted: StrictBool | None = None
    RequestResponses: list[FirehosePutRecordBatchResponseEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
