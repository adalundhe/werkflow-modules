from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_tag import NetworkManagerTag


class NetworkManagerTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: list[NetworkManagerTag]
