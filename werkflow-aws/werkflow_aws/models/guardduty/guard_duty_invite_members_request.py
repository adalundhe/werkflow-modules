from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GuardDutyInviteMembersRequest(BaseModel):
    DetectorId: StrictStr
    AccountIds: list[StrictStr]
    DisableEmailNotification: StrictBool | None = None
    Message: StrictStr | None = None
