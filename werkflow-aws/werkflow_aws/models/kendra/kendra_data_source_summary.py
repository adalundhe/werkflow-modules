from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KendraDataSourceSummary(BaseModel):
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    Type: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    LanguageCode: StrictStr | None = None
