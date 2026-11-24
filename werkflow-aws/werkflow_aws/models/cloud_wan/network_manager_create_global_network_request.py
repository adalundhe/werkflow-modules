from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_tag import NetworkManagerTag


class NetworkManagerCreateGlobalNetworkRequest(BaseModel):
    Description: StrictStr | None = None
    Tags: list[NetworkManagerTag] | None = None
