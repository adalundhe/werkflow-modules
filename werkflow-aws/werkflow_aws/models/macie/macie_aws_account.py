from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieAwsAccount(BaseModel):
    accountId: StrictStr | None = None
    principalId: StrictStr | None = None
