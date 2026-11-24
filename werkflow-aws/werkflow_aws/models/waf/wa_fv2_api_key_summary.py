from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class WAFv2APIKeySummary(BaseModel):
    TokenDomains: list[StrictStr] | None = None
    APIKey: StrictStr | None = None
    CreationTimestamp: datetime.datetime | StrictStr | None = None
    Version: StrictInt | None = None
