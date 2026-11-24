from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubFindingHistoryUpdateSource(BaseModel):
    Type: StrictStr | None = None
    Identity: StrictStr | None = None
