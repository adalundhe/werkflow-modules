from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .macie_session_context import MacieSessionContext


class MacieFederatedUser(BaseModel):
    accessKeyId: StrictStr | None = None
    accountId: StrictStr | None = None
    arn: StrictStr | None = None
    principalId: StrictStr | None = None
    sessionContext: MacieSessionContext | None = None
