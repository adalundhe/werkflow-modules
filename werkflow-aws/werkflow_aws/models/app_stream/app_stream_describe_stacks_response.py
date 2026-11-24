from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_stream_stack import AppStreamStack


class AppStreamDescribeStacksResponse(BaseModel):
    Stacks: list[AppStreamStack] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
