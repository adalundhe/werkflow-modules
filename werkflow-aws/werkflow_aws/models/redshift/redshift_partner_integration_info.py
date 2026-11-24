from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class RedshiftPartnerIntegrationInfo(BaseModel):
    DatabaseName: StrictStr | None = None
    PartnerName: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
