from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerPrefixListAssociation(BaseModel):
    CoreNetworkId: StrictStr | None = None
    PrefixListArn: StrictStr | None = None
    PrefixListAlias: StrictStr | None = None
