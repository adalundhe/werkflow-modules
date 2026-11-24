from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_stream_description_summary import KinesisStreamDescriptionSummary


class KinesisDescribeStreamSummaryResponse(BaseModel):
    StreamDescriptionSummary: KinesisStreamDescriptionSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
