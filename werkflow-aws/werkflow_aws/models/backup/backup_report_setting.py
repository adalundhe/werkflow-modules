from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BackupReportSetting(BaseModel):
    ReportTemplate: StrictStr | None = None
    FrameworkArns: list[StrictStr] | None = None
    NumberOfFrameworks: StrictInt | None = None
    Accounts: list[StrictStr] | None = None
    OrganizationUnits: list[StrictStr] | None = None
    Regions: list[StrictStr] | None = None
