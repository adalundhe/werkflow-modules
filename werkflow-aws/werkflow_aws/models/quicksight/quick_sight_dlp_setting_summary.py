from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QuickSightDlpSettingSummary(BaseModel):
    DlpSettingId: StrictStr | None = None
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    Status: StrictStr | None = None
    ProviderType: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
