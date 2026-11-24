from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_campaign import ConnectCampaign
from .connect_endpoint import ConnectEndpoint
from .connect_outbound_strategy import ConnectOutboundStrategy


class ConnectContactDataRequest(BaseModel):
    SystemEndpoint: ConnectEndpoint | None = None
    CustomerEndpoint: ConnectEndpoint | None = None
    RequestIdentifier: StrictStr | None = None
    QueueId: StrictStr | None = None
    Attributes: dict[StrictStr, StrictStr] | None = None
    Campaign: ConnectCampaign | None = None
    OutboundStrategy: ConnectOutboundStrategy | None = None
