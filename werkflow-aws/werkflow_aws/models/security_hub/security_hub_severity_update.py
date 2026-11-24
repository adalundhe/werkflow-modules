from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class SecurityHubSeverityUpdate(BaseModel):
    Normalized: StrictInt | None = None
    Product: StrictFloat | StrictInt | None = None
    Label: StrictStr | None = None
