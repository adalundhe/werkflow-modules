from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_provider_config import QuickSightProviderConfig


class QuickSightDlpSettingDetails(BaseModel):
    DlpSettingId: StrictStr | None = None
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    Status: StrictStr | None = None
    ProviderType: StrictStr | None = None
    ProviderConfig: QuickSightProviderConfig | None = None
    ProviderOutageAction: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
