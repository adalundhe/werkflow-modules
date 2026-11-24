from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MWAAIdentityCenterConfiguration(BaseModel):
    StartUrl: StrictStr | None = None
    IdentityStoreId: StrictStr | None = None
