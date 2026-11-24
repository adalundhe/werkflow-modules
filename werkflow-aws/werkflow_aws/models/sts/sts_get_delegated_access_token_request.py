from __future__ import annotations
from pydantic import BaseModel, StrictStr


class STSGetDelegatedAccessTokenRequest(BaseModel):
    TradeInToken: StrictStr
