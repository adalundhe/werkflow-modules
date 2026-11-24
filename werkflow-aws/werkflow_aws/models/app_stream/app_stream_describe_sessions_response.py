from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_stream_session import AppStreamSession


class AppStreamDescribeSessionsResponse(BaseModel):
    Sessions: list[AppStreamSession] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
