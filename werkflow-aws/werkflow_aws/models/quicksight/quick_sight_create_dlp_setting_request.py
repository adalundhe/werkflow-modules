from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .quick_sight_provider_config import QuickSightProviderConfig
from .quick_sight_tag import QuickSightTag


class QuickSightCreateDlpSettingRequest(BaseModel):
    AwsAccountId: StrictStr
    DlpSettingId: StrictStr
    Name: StrictStr
    ProviderType: Literal['MICROSOFT_PURVIEW']
    ProviderConfig: QuickSightProviderConfig
    ProviderOutageAction: Literal['ALLOW', 'WARN', 'BLOCK']
    Enabled: StrictBool
    Tags: list[QuickSightTag] | None = None
