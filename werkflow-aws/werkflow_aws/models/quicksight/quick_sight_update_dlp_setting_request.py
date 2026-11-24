from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .quick_sight_provider_config import QuickSightProviderConfig


class QuickSightUpdateDlpSettingRequest(BaseModel):
    AwsAccountId: StrictStr
    DlpSettingId: StrictStr
    Name: StrictStr | None = None
    ProviderType: Literal['MICROSOFT_PURVIEW'] | None = None
    ProviderConfig: QuickSightProviderConfig | None = None
    ProviderOutageAction: Literal['ALLOW', 'WARN', 'BLOCK'] | None = None
    Enabled: StrictBool | None = None
