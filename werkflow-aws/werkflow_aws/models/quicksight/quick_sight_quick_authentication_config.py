from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_quick_authentication_configuration_detail import QuickSightQuickAuthenticationConfigurationDetail


class QuickSightQuickAuthenticationConfig(BaseModel):
    QuickAuthenticationType: StrictStr | None = None
    QuickAuthenticationConfigurationDetail: QuickSightQuickAuthenticationConfigurationDetail | None = None
