from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_context_store_association import NetworkManagerContextStoreAssociation


class NetworkManagerListContextStoreAssociationsResponse(BaseModel):
    ContextStoreAssociations: list[NetworkManagerContextStoreAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
