from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_stream_stack import AppStreamStack


class AppStreamCreateStackResponse(BaseModel):
    Stack: AppStreamStack | None = None
    ResponseMetadata: dict[str, Any] | None = None
