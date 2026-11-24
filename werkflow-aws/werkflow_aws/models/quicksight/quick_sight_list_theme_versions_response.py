from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_theme_version_summary import QuickSightThemeVersionSummary


class QuickSightListThemeVersionsResponse(BaseModel):
    ThemeVersionSummaryList: list[QuickSightThemeVersionSummary] | None = None
    NextToken: StrictStr | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
