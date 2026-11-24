from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteDlpSettingRequest(BaseModel):
    AwsAccountId: StrictStr
    DlpSettingId: StrictStr
