from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .direct_connect_tag import DirectConnectTag


class DirectConnectCreateInterconnectRequest(BaseModel):
    interconnectName: StrictStr
    bandwidth: StrictStr
    location: StrictStr
    lagId: StrictStr | None = None
    tags: list[DirectConnectTag] | None = None
    providerName: StrictStr | None = None
    requestMACSec: StrictBool | None = None
