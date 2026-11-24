from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_record_configuration import KinesisRecordConfiguration


class KinesisChannelStreamConfiguration(BaseModel):
    StreamARN: StrictStr
    RecordConfiguration: KinesisRecordConfiguration
