from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubRecord(BaseModel):
    JsonPath: StrictStr | None = None
    RecordIndex: StrictInt | None = None
