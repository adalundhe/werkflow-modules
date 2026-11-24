from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftAccountWithRestoreAccess(BaseModel):
    AccountId: StrictStr | None = None
    AccountAlias: StrictStr | None = None
