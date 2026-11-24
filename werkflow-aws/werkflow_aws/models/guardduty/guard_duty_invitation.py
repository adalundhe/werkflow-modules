from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyInvitation(BaseModel):
    AccountId: StrictStr | None = None
    InvitationId: StrictStr | None = None
    RelationshipStatus: StrictStr | None = None
    InvitedAt: StrictStr | None = None
