from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubErrorDetail(BaseModel):
    errorMessage: StrictStr | None = None
