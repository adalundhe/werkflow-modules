from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_inbound_connector_config import QuickSightInboundConnectorConfig


class QuickSightUpdateInboundConnectorRequest(BaseModel):
    AwsAccountId: StrictStr
    InboundConnectorId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    InboundConnectorConfiguration: QuickSightInboundConnectorConfig | None = None
    InboundConnectorStatus: Literal['ENABLED', 'DISABLED'] | None = None
