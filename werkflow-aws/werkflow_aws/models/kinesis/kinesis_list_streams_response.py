from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .kinesis_stream_summary import KinesisStreamSummary


class KinesisListStreamsResponse(BaseModel):
    StreamNames: list[StrictStr] | None = None
    HasMoreStreams: StrictBool | None = None
    NextToken: StrictStr | None = None
    StreamSummaries: list[KinesisStreamSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
