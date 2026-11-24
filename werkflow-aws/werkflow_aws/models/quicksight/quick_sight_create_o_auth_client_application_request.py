from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_tag import QuickSightTag
from .quick_sight_vpc_connection_properties import QuickSightVpcConnectionProperties


class QuickSightCreateOAuthClientApplicationRequest(BaseModel):
    AwsAccountId: StrictStr
    OAuthClientApplicationId: StrictStr
    Name: StrictStr
    OAuthClientAuthenticationType: Literal['TOKEN']
    ClientId: StrictStr
    ClientSecret: StrictStr
    OAuthTokenEndpointUrl: StrictStr
    OAuthAuthorizationEndpointUrl: StrictStr | None = None
    OAuthScopes: StrictStr | None = None
    DataSourceType: StrictStr | None = None
    IdentityProviderVpcConnectionProperties: QuickSightVpcConnectionProperties | None = None
    Tags: list[QuickSightTag] | None = None
