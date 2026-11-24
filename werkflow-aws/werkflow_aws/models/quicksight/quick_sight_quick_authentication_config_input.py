from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .quick_sight_quick_authentication_configuration_detail_input import QuickSightQuickAuthenticationConfigurationDetailInput


class QuickSightQuickAuthenticationConfigInput(BaseModel):
    QuickAuthenticationType: Literal['QUICK_MANAGED_PUBLIC_AUTH_CODE']
    QuickAuthenticationConfigurationDetailInput: QuickSightQuickAuthenticationConfigurationDetailInput | None = None
