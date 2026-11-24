from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_attachment import NetworkManagerAttachment


class NetworkManagerSiteToSiteVpnAttachment(BaseModel):
    Attachment: NetworkManagerAttachment | None = None
    VpnConnectionArn: StrictStr | None = None
