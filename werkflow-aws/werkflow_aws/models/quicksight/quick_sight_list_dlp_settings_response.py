from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_dlp_setting_summary import QuickSightDlpSettingSummary


class QuickSightListDlpSettingsResponse(BaseModel):
    DlpSettingSummaries: list[QuickSightDlpSettingSummary] | None = None
    NextToken: StrictStr | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
