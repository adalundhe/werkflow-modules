from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ServiceCatalogResourceDetail(BaseModel):
    Id: StrictStr | None = None
    ARN: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
