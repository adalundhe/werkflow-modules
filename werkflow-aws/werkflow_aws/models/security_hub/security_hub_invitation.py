from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SecurityHubInvitation(BaseModel):
    AccountId: StrictStr | None = None
    InvitationId: StrictStr | None = None
    InvitedAt: datetime.datetime | StrictStr | None = None
    MemberStatus: StrictStr | None = None
