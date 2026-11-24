from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMUntagOpenIDConnectProviderRequest(BaseModel):
    OpenIDConnectProviderArn: StrictStr
    TagKeys: list[StrictStr]
