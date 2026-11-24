from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesCreateAccountLinkInvitationRequest(BaseModel):
    TargetAccountId: StrictStr
    ClientToken: StrictStr | None = None
