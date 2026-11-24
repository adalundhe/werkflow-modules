from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .kinesis_stream_mode_details import KinesisStreamModeDetails


class KinesisStreamSummary(BaseModel):
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    StreamStatus: StrictStr | None = None
    StreamModeDetails: KinesisStreamModeDetails | None = None
    StreamCreationTimestamp: datetime.datetime | StrictStr | None = None
