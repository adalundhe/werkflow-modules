from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_link import NetworkManagerLink


class NetworkManagerUpdateLinkResponse(BaseModel):
    Link: NetworkManagerLink | None = None
    ResponseMetadata: dict[str, Any] | None = None
