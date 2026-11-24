from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_view_version_summary import ConnectViewVersionSummary


class ConnectListViewVersionsResponse(BaseModel):
    ViewVersionSummaryList: list[ConnectViewVersionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
