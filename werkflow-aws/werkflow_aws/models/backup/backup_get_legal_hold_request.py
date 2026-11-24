from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupGetLegalHoldRequest(BaseModel):
    LegalHoldId: StrictStr
