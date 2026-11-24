from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SecurityHubMember(BaseModel):
    AccountId: StrictStr | None = None
    Email: StrictStr | None = None
    MasterId: StrictStr | None = None
    AdministratorId: StrictStr | None = None
    MemberStatus: StrictStr | None = None
    InvitedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
