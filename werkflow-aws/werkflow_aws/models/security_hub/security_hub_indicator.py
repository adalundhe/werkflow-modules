from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubIndicator(BaseModel):
    Key: StrictStr | None = None
    Values: list[StrictStr] | None = None
    Title: StrictStr | None = None
    Type: StrictStr | None = None
