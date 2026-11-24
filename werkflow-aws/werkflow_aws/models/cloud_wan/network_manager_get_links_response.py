from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_link import NetworkManagerLink


class NetworkManagerGetLinksResponse(BaseModel):
    Links: list[NetworkManagerLink] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
