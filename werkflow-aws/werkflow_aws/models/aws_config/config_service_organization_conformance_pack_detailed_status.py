from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConfigServiceOrganizationConformancePackDetailedStatus(BaseModel):
    AccountId: StrictStr | None = None
    ConformancePackName: StrictStr | None = None
    Status: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
