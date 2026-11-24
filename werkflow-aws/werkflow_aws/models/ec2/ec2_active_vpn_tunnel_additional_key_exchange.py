from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2ActiveVpnTunnelAdditionalKeyExchange(BaseModel):
    AdditionalKeyExchangeRound: StrictInt | None = None
    KeyExchangeMethod: StrictInt | None = None
