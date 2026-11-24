from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMUpdateOpenIDConnectProviderThumbprintRequest(BaseModel):
    OpenIDConnectProviderArn: StrictStr
    ThumbprintList: list[StrictStr]
