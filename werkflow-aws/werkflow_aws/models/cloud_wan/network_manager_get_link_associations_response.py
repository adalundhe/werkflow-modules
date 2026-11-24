from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_link_association import NetworkManagerLinkAssociation


class NetworkManagerGetLinkAssociationsResponse(BaseModel):
    LinkAssociations: list[NetworkManagerLinkAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
