from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class PinpointSMSChannelRequest(BaseModel):
    Enabled: StrictBool | None = None
    SenderId: StrictStr | None = None
    ShortCode: StrictStr | None = None
