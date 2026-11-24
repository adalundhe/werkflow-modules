from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_idp_authorizing_config_update_input import QuickSightIdpAuthorizingConfigUpdateInput
from .quick_sight_quick_authentication_config_input import QuickSightQuickAuthenticationConfigInput


class QuickSightUpdateAccessControlApplicationRequest(BaseModel):
    AwsAccountId: StrictStr
    ApplicationId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    IdpAuthorizingConfiguration: QuickSightIdpAuthorizingConfigUpdateInput | None = None
    QuickAuthenticationConfiguration: QuickSightQuickAuthenticationConfigInput | None = None
    Status: Literal['ENABLED', 'DISABLED'] | None = None
