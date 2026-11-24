from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubKeywordFilter(BaseModel):
    Value: StrictStr | None = None
