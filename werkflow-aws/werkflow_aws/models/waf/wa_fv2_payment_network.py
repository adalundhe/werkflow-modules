from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_price import WAFv2Price


class WAFv2PaymentNetwork(BaseModel):
    Chain: StrictStr | None = None
    WalletAddress: StrictStr | None = None
    Prices: list[WAFv2Price] | None = None
