from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAuthorizationCodeGrantDetails(BaseModel):
    ClientId: StrictStr
    ClientSecret: StrictStr
    TokenEndpoint: StrictStr
    AuthorizationEndpoint: StrictStr
