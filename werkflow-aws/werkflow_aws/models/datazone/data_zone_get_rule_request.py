from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetRuleRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    revision: StrictStr | None = None
