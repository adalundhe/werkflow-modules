from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BackupLatestMpaApprovalTeamUpdate(BaseModel):
    MpaSessionArn: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    InitiationDate: datetime.datetime | StrictStr | None = None
    ExpiryDate: datetime.datetime | StrictStr | None = None
