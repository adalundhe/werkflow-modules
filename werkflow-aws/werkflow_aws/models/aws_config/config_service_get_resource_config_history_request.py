from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConfigServiceGetResourceConfigHistoryRequest(BaseModel):
    resourceType: StrictStr
    resourceId: StrictStr
    laterTime: datetime.datetime | StrictStr | None = None
    earlierTime: datetime.datetime | StrictStr | None = None
    chronologicalOrder: Literal['Reverse', 'Forward'] | None = None
    limit: StrictInt | None = None
    nextToken: StrictStr | None = None
