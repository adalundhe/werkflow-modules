from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubNote(BaseModel):
    Text: StrictStr | None = None
    UpdatedBy: StrictStr | None = None
    UpdatedAt: StrictStr | None = None
