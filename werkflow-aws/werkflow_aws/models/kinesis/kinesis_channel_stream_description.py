from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .kinesis_record_configuration import KinesisRecordConfiguration


class KinesisChannelStreamDescription(BaseModel):
    StreamARN: StrictStr | None = None
    StreamCreationTimestamp: datetime.datetime | StrictStr | None = None
    RecordConfiguration: KinesisRecordConfiguration | None = None
