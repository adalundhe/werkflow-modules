from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPGetIdentityProviderByIdentifierRequest(BaseModel):
    UserPoolId: StrictStr
    IdpIdentifier: StrictStr
