from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteRuleRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
