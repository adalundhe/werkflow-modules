from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerDeleteSiteRequest(BaseModel):
    GlobalNetworkId: StrictStr
    SiteId: StrictStr
