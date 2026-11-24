from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubRecommendationError(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
