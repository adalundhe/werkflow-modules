from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_stream_application import AppStreamApplication


class AppStreamDescribeApplicationsResponse(BaseModel):
    Applications: list[AppStreamApplication] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
