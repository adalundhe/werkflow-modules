from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerCreateCoreNetworkPrefixListAssociationRequest(BaseModel):
    CoreNetworkId: StrictStr
    PrefixListArn: StrictStr
    PrefixListAlias: StrictStr
    ClientToken: StrictStr | None = None
