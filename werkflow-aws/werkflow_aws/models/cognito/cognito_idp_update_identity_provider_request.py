from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPUpdateIdentityProviderRequest(BaseModel):
    UserPoolId: StrictStr
    ProviderName: StrictStr
    ProviderDetails: dict[StrictStr, StrictStr] | None = None
    AttributeMapping: dict[StrictStr, StrictStr] | None = None
    IdpIdentifiers: list[StrictStr] | None = None
    AcrMapping: dict[StrictStr, StrictStr] | None = None
