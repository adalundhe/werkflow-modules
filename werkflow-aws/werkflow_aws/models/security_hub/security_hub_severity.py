from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class SecurityHubSeverity(BaseModel):
    Product: StrictFloat | StrictInt | None = None
    Label: StrictStr | None = None
    Normalized: StrictInt | None = None
    Original: StrictStr | None = None
