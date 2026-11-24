from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowOAuth2Properties(BaseModel):
    tokenUrl: StrictStr | None = None
    oAuth2GrantType: StrictStr | None = None
    tokenUrlCustomProperties: dict[StrictStr, StrictStr] | None = None
