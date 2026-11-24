from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class FMSResourceSet(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    UpdateToken: StrictStr | None = None
    ResourceTypeList: list[StrictStr] | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
    ResourceSetStatus: StrictStr | None = None
