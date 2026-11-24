from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_vpc_connection_properties import QuickSightVpcConnectionProperties


class QuickSightUpdateOAuthClientApplicationRequest(BaseModel):
    AwsAccountId: StrictStr
    OAuthClientApplicationId: StrictStr
    Name: StrictStr
    ClientId: StrictStr | None = None
    ClientSecret: StrictStr | None = None
    OAuthTokenEndpointUrl: StrictStr | None = None
    OAuthAuthorizationEndpointUrl: StrictStr | None = None
    OAuthScopes: StrictStr | None = None
    DataSourceType: StrictStr | None = None
    IdentityProviderVpcConnectionProperties: QuickSightVpcConnectionProperties | None = None
