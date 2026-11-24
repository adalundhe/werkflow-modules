from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class MacieUserPausedDetails(BaseModel):
    jobExpiresAt: datetime.datetime | StrictStr | None = None
    jobImminentExpirationHealthEventArn: StrictStr | None = None
    jobPausedAt: datetime.datetime | StrictStr | None = None
