from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_stream_mode_details import KinesisStreamModeDetails


class KinesisUpdateStreamModeRequest(BaseModel):
    StreamARN: StrictStr
    StreamModeDetails: KinesisStreamModeDetails
    StreamId: StrictStr | None = None
    WarmThroughputMiBps: StrictInt | None = None
