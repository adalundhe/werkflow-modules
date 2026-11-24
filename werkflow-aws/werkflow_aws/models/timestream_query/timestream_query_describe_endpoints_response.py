from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .timestream_query_endpoint import TimestreamQueryEndpoint


class TimestreamQueryDescribeEndpointsResponse(BaseModel):
    Endpoints: list[TimestreamQueryEndpoint] | None = None
    ResponseMetadata: dict[str, Any] | None = None
