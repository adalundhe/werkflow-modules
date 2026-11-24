from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubNoteUpdate(BaseModel):
    Text: StrictStr | None = None
    UpdatedBy: StrictStr | None = None
