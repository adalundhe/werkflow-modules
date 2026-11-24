from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyMember(BaseModel):
    AccountId: StrictStr | None = None
    DetectorId: StrictStr | None = None
    MasterId: StrictStr | None = None
    Email: StrictStr | None = None
    RelationshipStatus: StrictStr | None = None
    InvitedAt: StrictStr | None = None
    UpdatedAt: StrictStr | None = None
    AdministratorId: StrictStr | None = None
