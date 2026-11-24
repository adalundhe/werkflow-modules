from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KendraIndexConfigurationSummary(BaseModel):
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    Edition: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
