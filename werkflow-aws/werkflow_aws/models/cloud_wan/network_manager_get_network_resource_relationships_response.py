from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_relationship import NetworkManagerRelationship


class NetworkManagerGetNetworkResourceRelationshipsResponse(BaseModel):
    Relationships: list[NetworkManagerRelationship] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
