from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_inbound_connector_config import QuickSightInboundConnectorConfig


class QuickSightInboundConnector(BaseModel):
    InboundConnectorId: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    TenantUrl: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    InboundConnectorConfiguration: QuickSightInboundConnectorConfig | None = None
    Description: StrictStr | None = None
