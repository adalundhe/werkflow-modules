from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_view_summary import ConnectViewSummary


class ConnectListViewsResponse(BaseModel):
    ViewsSummaryList: list[ConnectViewSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
