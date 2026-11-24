from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CognitoIDPGetDerivedTokenRequest(BaseModel):
    ClientId: StrictStr
    SubjectToken: StrictStr
    SubjectTokenType: Literal['ACCESS_TOKEN', 'ID_TOKEN', 'SAML2']
    ClientSecret: StrictStr | None = None
    SubjectTokenProviderName: StrictStr | None = None
    ActorToken: StrictStr | None = None
    ActorTokenType: Literal['ACCESS_TOKEN', 'ID_TOKEN', 'SAML2'] | None = None
    ActorTokenProviderName: StrictStr | None = None
    Scopes: list[StrictStr] | None = None
    Audiences: list[StrictStr] | None = None
    Resources: list[StrictStr] | None = None
    RequestedTokenType: Literal['ACCESS_TOKEN', 'ID_TOKEN'] | None = None
