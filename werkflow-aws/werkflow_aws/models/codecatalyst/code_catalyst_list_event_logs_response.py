from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_catalyst_event_log_entry import CodeCatalystEventLogEntry


class CodeCatalystListEventLogsResponse(BaseModel):
    nextToken: StrictStr | None = None
    items: list[CodeCatalystEventLogEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
