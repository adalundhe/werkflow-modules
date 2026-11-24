from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_failed_request import ConnectFailedRequest
from .connect_successful_request import ConnectSuccessfulRequest


class ConnectBatchPutContactResponse(BaseModel):
    SuccessfulRequestList: list[ConnectSuccessfulRequest] | None = None
    FailedRequestList: list[ConnectFailedRequest] | None = None
    ResponseMetadata: dict[str, Any] | None = None
