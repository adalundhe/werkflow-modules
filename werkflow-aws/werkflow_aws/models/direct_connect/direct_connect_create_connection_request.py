from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .direct_connect_tag import DirectConnectTag


class DirectConnectCreateConnectionRequest(BaseModel):
    location: StrictStr
    bandwidth: StrictStr
    connectionName: StrictStr
    lagId: StrictStr | None = None
    tags: list[DirectConnectTag] | None = None
    providerName: StrictStr | None = None
    requestMACSec: StrictBool | None = None
    billingMode: Literal['PayAsYouGo', 'FlatRateTier1', 'FlatRateTier2', 'FlatRateTier3', 'FlatRateTier4', 'FlatRateTier5'] | None = None
