from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_site import NetworkManagerSite


class NetworkManagerCreateSiteResponse(BaseModel):
    Site: NetworkManagerSite | None = None
    ResponseMetadata: dict[str, Any] | None = None
