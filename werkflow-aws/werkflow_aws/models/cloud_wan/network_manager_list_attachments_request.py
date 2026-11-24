from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerListAttachmentsRequest(BaseModel):
    CoreNetworkId: StrictStr | None = None
    AttachmentType: Literal['CONNECT', 'SITE_TO_SITE_VPN', 'VPC', 'DIRECT_CONNECT_GATEWAY', 'TRANSIT_GATEWAY_ROUTE_TABLE'] | None = None
    EdgeLocation: StrictStr | None = None
    State: Literal['REJECTED', 'PENDING_ATTACHMENT_ACCEPTANCE', 'CREATING', 'FAILED', 'AVAILABLE', 'UPDATING', 'PENDING_NETWORK_UPDATE', 'PENDING_TAG_ACCEPTANCE', 'DELETING'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
