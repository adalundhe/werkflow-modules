from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CognitoIDPCreateIdentityProviderRequest(BaseModel):
    UserPoolId: StrictStr
    ProviderName: StrictStr
    ProviderType: Literal['SAML', 'Facebook', 'Google', 'LoginWithAmazon', 'SignInWithApple', 'OIDC']
    ProviderDetails: dict[StrictStr, StrictStr]
    AttributeMapping: dict[StrictStr, StrictStr] | None = None
    IdpIdentifiers: list[StrictStr] | None = None
    AcrMapping: dict[StrictStr, StrictStr] | None = None
