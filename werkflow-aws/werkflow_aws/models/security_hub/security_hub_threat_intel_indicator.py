from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubThreatIntelIndicator(BaseModel):
    Type: StrictStr | None = None
    Value: StrictStr | None = None
    Category: StrictStr | None = None
    LastObservedAt: StrictStr | None = None
    Source: StrictStr | None = None
    SourceUrl: StrictStr | None = None
