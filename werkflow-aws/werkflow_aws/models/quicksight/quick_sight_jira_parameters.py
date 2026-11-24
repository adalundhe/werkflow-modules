from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightJiraParameters(BaseModel):
    SiteBaseUrl: StrictStr | None = None
