from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesDeleteAccountLinkInvitationRequest(BaseModel):
    LinkId: StrictStr
    ClientToken: StrictStr | None = None
