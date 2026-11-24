from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_connected_account_config import WAFv2ConnectedAccountConfig
from .wa_fv2_crypto_config import WAFv2CryptoConfig


class WAFv2MonetizationConfig(BaseModel):
    CryptoConfig: WAFv2CryptoConfig | None = None
    ConnectedAccountConfigs: list[WAFv2ConnectedAccountConfig] | None = None
    CurrencyMode: StrictStr | None = None
