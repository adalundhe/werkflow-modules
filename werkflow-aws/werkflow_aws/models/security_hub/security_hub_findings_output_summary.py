from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubFindingsOutputSummary(BaseModel):
    Format: StrictStr | None = None
