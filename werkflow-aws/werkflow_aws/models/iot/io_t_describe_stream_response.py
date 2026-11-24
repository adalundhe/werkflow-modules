from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .io_t_stream_info import IoTStreamInfo


class IoTDescribeStreamResponse(BaseModel):
    streamInfo: IoTStreamInfo | None = None
    ResponseMetadata: dict[str, Any] | None = None
