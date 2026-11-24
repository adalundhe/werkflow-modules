from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_quick_authentication_configuration_detail_create_output import QuickSightQuickAuthenticationConfigurationDetailCreateOutput


class QuickSightQuickAuthenticationConfigCreateOutput(BaseModel):
    QuickAuthenticationType: StrictStr | None = None
    QuickAuthenticationConfigurationDetailCreateOutput: QuickSightQuickAuthenticationConfigurationDetailCreateOutput | None = None
