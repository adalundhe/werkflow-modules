from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMAddClientIDToOpenIDConnectProviderRequest(BaseModel):
    OpenIDConnectProviderArn: StrictStr
    ClientID: StrictStr
