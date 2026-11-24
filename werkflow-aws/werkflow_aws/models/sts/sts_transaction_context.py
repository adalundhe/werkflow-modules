from __future__ import annotations
from pydantic import BaseModel, StrictStr


class STSTransactionContext(BaseModel):
    IdentityProvider: dict[StrictStr, StrictStr] | None = None
