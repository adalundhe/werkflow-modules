from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_legal_hold import BackupLegalHold


class BackupListLegalHoldsResponse(BaseModel):
    NextToken: StrictStr | None = None
    LegalHolds: list[BackupLegalHold] | None = None
    ResponseMetadata: dict[str, Any] | None = None
