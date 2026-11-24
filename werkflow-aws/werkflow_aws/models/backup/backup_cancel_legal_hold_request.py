from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BackupCancelLegalHoldRequest(BaseModel):
    LegalHoldId: StrictStr
    CancelDescription: StrictStr
    RetainRecordInDays: StrictInt | None = None
