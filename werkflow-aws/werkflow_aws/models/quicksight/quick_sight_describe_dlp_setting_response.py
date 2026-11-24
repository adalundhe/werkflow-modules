from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_dlp_setting_details import QuickSightDlpSettingDetails


class QuickSightDescribeDlpSettingResponse(BaseModel):
    DlpSetting: QuickSightDlpSettingDetails | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
