from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDeleteOpenIDConnectProviderRequest(BaseModel):
    OpenIDConnectProviderArn: StrictStr
