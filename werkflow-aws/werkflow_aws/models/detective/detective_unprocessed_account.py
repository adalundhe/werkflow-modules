from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveUnprocessedAccount(BaseModel):
    AccountId: StrictStr | None = None
    Reason: StrictStr | None = None
