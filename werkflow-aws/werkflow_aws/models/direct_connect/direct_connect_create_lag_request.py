from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .direct_connect_tag import DirectConnectTag


class DirectConnectCreateLagRequest(BaseModel):
    numberOfConnections: StrictInt
    location: StrictStr
    connectionsBandwidth: StrictStr
    lagName: StrictStr
    connectionId: StrictStr | None = None
    tags: list[DirectConnectTag] | None = None
    childConnectionTags: list[DirectConnectTag] | None = None
    providerName: StrictStr | None = None
    requestMACSec: StrictBool | None = None
    billingMode: Literal['PayAsYouGo', 'FlatRateTier1', 'FlatRateTier2', 'FlatRateTier3', 'FlatRateTier4', 'FlatRateTier5'] | None = None
