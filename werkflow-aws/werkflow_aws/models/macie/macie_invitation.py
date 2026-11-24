from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class MacieInvitation(BaseModel):
    accountId: StrictStr | None = None
    invitationId: StrictStr | None = None
    invitedAt: datetime.datetime | StrictStr | None = None
    relationshipStatus: StrictStr | None = None
