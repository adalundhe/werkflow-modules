from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class QuickSightUpdateDlpSettingResponse(BaseModel):
    Arn: StrictStr | None = None
    DlpSettingId: StrictStr | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
