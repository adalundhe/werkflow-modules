from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KendraFaqSummary(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    FileFormat: StrictStr | None = None
    LanguageCode: StrictStr | None = None
