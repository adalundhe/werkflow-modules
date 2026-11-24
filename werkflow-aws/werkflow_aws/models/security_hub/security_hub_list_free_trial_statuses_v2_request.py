from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubListFreeTrialStatusesV2Request(BaseModel):
    AccountIds: list[StrictStr] | None = None
    Statuses: list[Literal['ACTIVE', 'INACTIVE']] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
