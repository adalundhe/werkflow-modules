from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_connected_account_chain_config import WAFv2ConnectedAccountChainConfig


class WAFv2ConnectedAccountConfig(BaseModel):
    ConnectedAccountArn: StrictStr | None = None
    PaymentNetworks: list[WAFv2ConnectedAccountChainConfig] | None = None
