from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesAcceptAccountLinkInvitationRequest(BaseModel):
    LinkId: StrictStr
    ClientToken: StrictStr | None = None
