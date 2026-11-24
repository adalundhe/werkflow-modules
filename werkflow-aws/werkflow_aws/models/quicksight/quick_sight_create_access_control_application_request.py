from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_idp_authorizing_config_input import QuickSightIdpAuthorizingConfigInput
from .quick_sight_quick_authentication_config_input import QuickSightQuickAuthenticationConfigInput
from .quick_sight_tag import QuickSightTag


class QuickSightCreateAccessControlApplicationRequest(BaseModel):
    AwsAccountId: StrictStr
    ApplicationId: StrictStr
    Name: StrictStr
    Namespace: StrictStr
    AuthenticationType: Literal['OIDC']
    IdpAuthorizingConfiguration: QuickSightIdpAuthorizingConfigInput
    QuickAuthenticationConfiguration: QuickSightQuickAuthenticationConfigInput
    Description: StrictStr | None = None
    Tags: list[QuickSightTag] | None = None
