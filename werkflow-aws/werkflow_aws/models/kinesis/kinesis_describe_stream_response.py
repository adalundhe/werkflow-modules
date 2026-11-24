from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_stream_description import KinesisStreamDescription


class KinesisDescribeStreamResponse(BaseModel):
    StreamDescription: KinesisStreamDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
