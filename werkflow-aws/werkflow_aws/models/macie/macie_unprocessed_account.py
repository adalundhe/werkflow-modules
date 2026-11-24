from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieUnprocessedAccount(BaseModel):
    accountId: StrictStr | None = None
    errorCode: StrictStr | None = None
    errorMessage: StrictStr | None = None
