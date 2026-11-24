from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyListCustomDetectionRuleAssociationsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    RuleId: StrictStr | None = None
    Mode: Literal['LIVE', 'DRY_RUN'] | None = None
