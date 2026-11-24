from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .timestream_write_endpoint import TimestreamWriteEndpoint


class TimestreamWriteDescribeEndpointsResponse(BaseModel):
    Endpoints: list[TimestreamWriteEndpoint] | None = None
    ResponseMetadata: dict[str, Any] | None = None
