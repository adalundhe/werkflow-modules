from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSDiscoveredResource(BaseModel):
    URI: StrictStr | None = None
    AccountId: StrictStr | None = None
    Type: StrictStr | None = None
    Name: StrictStr | None = None
