from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubRecommendation(BaseModel):
    Text: StrictStr | None = None
    Url: StrictStr | None = None
