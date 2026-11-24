from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class WAFv2UpdateManagedRuleSetVersionExpiryDateRequest(BaseModel):
    Name: StrictStr
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    Id: StrictStr
    LockToken: StrictStr
    VersionToExpire: StrictStr
    ExpiryTimestamp: datetime.datetime | StrictStr
