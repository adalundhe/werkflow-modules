from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class IAMAccessDetail(BaseModel):
    ServiceName: StrictStr | None = None
    ServiceNamespace: StrictStr | None = None
    Region: StrictStr | None = None
    EntityPath: StrictStr | None = None
    LastAuthenticatedTime: datetime.datetime | StrictStr | None = None
    TotalAuthenticatedEntities: StrictInt | None = None
