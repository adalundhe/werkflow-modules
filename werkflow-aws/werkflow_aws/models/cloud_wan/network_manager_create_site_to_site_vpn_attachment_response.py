from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_site_to_site_vpn_attachment import NetworkManagerSiteToSiteVpnAttachment


class NetworkManagerCreateSiteToSiteVpnAttachmentResponse(BaseModel):
    SiteToSiteVpnAttachment: NetworkManagerSiteToSiteVpnAttachment | None = None
    ResponseMetadata: dict[str, Any] | None = None
