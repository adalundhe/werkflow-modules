from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BackupLegalHold(BaseModel):
    Title: StrictStr | None = None
    Status: StrictStr | None = None
    Description: StrictStr | None = None
    LegalHoldId: StrictStr | None = None
    LegalHoldArn: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    CancellationDate: datetime.datetime | StrictStr | None = None
