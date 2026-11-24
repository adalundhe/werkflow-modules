from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightServiceNowParameters(BaseModel):
    SiteBaseUrl: StrictStr | None = None
