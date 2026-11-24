from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class NetworkManagerCreateCoreNetworkPrefixListAssociationResponse(BaseModel):
    CoreNetworkId: StrictStr | None = None
    PrefixListArn: StrictStr | None = None
    PrefixListAlias: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
