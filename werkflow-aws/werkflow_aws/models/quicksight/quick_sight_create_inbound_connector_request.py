from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_inbound_connector_config import QuickSightInboundConnectorConfig
from .quick_sight_tag import QuickSightTag


class QuickSightCreateInboundConnectorRequest(BaseModel):
    AwsAccountId: StrictStr
    InboundConnectorId: StrictStr
    Name: StrictStr
    InboundConnectorConfiguration: QuickSightInboundConnectorConfig
    Description: StrictStr | None = None
    Tags: list[QuickSightTag] | None = None
