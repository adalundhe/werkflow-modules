from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMAzureSubscription(BaseModel):
    Id: StrictStr | None = None
    DisplayName: StrictStr | None = None
