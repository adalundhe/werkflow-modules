from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_link_association import NetworkManagerLinkAssociation


class NetworkManagerDisassociateLinkResponse(BaseModel):
    LinkAssociation: NetworkManagerLinkAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
