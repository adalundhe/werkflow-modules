from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_app_summary import QuickSightAppSummary


class QuickSightListAppsResponse(BaseModel):
    AppSummaryList: list[QuickSightAppSummary] | None = None
    NextToken: StrictStr | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
