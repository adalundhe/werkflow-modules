from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerDeleteCoreNetworkPrefixListAssociationRequest(BaseModel):
    CoreNetworkId: StrictStr
    PrefixListArn: StrictStr
