from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyOrganizationFeatureStatisticsAdditionalConfiguration(BaseModel):
    Name: StrictStr | None = None
    EnabledAccountsCount: StrictInt | None = None
