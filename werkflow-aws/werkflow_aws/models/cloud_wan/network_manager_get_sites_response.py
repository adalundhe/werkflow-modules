from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_site import NetworkManagerSite


class NetworkManagerGetSitesResponse(BaseModel):
    Sites: list[NetworkManagerSite] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
