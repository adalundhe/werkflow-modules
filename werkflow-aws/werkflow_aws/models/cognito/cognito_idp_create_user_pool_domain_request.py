from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cognito_idp_custom_domain_config_type import CognitoIDPCustomDomainConfigType
from .cognito_idp_routing_type import CognitoIDPRoutingType


class CognitoIDPCreateUserPoolDomainRequest(BaseModel):
    Domain: StrictStr
    UserPoolId: StrictStr
    ManagedLoginVersion: StrictInt | None = None
    CustomDomainConfig: CognitoIDPCustomDomainConfigType | None = None
    Routing: CognitoIDPRoutingType | None = None
