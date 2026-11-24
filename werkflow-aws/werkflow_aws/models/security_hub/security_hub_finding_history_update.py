from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubFindingHistoryUpdate(BaseModel):
    UpdatedField: StrictStr | None = None
    OldValue: StrictStr | None = None
    NewValue: StrictStr | None = None
