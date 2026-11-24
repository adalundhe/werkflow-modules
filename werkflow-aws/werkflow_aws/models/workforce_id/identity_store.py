from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IdentityStore(BaseModel):
    IdentityStoreId: StrictStr | None = None
    IdentityStoreArn: StrictStr | None = None
