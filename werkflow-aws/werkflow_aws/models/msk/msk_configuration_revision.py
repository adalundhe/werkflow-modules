from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class MSKConfigurationRevision(BaseModel):
    CreationTime: datetime.datetime | None = None
    Description: StrictStr | None = None
    Revision: StrictInt | None = None
