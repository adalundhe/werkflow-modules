from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMAccountSharingInfo(BaseModel):
    AccountId: StrictStr | None = None
    SharedDocumentVersion: StrictStr | None = None
