from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_outbound_strategy_config import ConnectOutboundStrategyConfig


class ConnectOutboundStrategy(BaseModel):
    Type: StrictStr | None = None
    Config: ConnectOutboundStrategyConfig | None = None
