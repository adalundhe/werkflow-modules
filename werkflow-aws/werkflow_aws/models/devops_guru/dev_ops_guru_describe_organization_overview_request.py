from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DevOpsGuruDescribeOrganizationOverviewRequest(BaseModel):
    FromTime: datetime.datetime | StrictStr
    ToTime: datetime.datetime | StrictStr | None = None
    AccountIds: list[StrictStr] | None = None
    OrganizationalUnitIds: list[StrictStr] | None = None
