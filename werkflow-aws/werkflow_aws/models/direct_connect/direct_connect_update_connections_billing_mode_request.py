from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DirectConnectUpdateConnectionsBillingModeRequest(BaseModel):
    connectionIds: list[StrictStr]
    billingMode: Literal['PayAsYouGo', 'FlatRateTier1', 'FlatRateTier2', 'FlatRateTier3', 'FlatRateTier4', 'FlatRateTier5']
