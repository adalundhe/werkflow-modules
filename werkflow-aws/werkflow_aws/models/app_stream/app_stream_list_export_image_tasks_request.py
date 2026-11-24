from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .app_stream_filter import AppStreamFilter


class AppStreamListExportImageTasksRequest(BaseModel):
    Filters: list[AppStreamFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
