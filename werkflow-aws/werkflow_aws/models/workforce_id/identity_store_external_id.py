from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IdentityStoreExternalId(BaseModel):
    Issuer: StrictStr | None = None
    Id: StrictStr | None = None
