from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MacieCreateInvitationsRequest(BaseModel):
    accountIds: list[StrictStr]
    disableEmailNotification: StrictBool | None = None
    message: StrictStr | None = None
