from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieUserIdentityRoot(BaseModel):
    accountId: StrictStr | None = None
    arn: StrictStr | None = None
    principalId: StrictStr | None = None
