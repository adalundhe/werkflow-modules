from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class MSKConfigurationRevisionModel(BaseModel):
    CreationTime: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    Revision: StrictInt | None = None
