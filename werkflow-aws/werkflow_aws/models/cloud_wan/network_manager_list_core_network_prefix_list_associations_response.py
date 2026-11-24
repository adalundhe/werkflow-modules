from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_prefix_list_association import NetworkManagerPrefixListAssociation


class NetworkManagerListCoreNetworkPrefixListAssociationsResponse(BaseModel):
    PrefixListAssociations: list[NetworkManagerPrefixListAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
