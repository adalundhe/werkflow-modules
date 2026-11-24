from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .kinesis_put_records_request_entry import KinesisPutRecordsRequestEntry


class KinesisPutRecordsRequest(BaseModel):
    Records: list[KinesisPutRecordsRequestEntry]
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    StreamId: StrictStr | None = None
    DryRun: StrictBool | None = None
