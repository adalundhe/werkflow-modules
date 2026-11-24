from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyListCustomDetectionRuleOrgConfigurationsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Status: Literal['ACTIVE', 'PROCESSING', 'FAILED'] | None = None
