from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_connected_account_price import WAFv2ConnectedAccountPrice


class WAFv2ConnectedAccountChainConfig(BaseModel):
    Chain: StrictStr | None = None
    Prices: list[WAFv2ConnectedAccountPrice] | None = None
