from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_payment_network import WAFv2PaymentNetwork


class WAFv2CryptoConfig(BaseModel):
    PaymentNetworks: list[WAFv2PaymentNetwork] | None = None
