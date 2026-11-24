from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMRemoveClientIDFromOpenIDConnectProviderRequest(BaseModel):
    OpenIDConnectProviderArn: StrictStr
    ClientID: StrictStr
