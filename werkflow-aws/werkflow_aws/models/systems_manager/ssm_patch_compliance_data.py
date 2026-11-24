from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SSMPatchComplianceData(BaseModel):
    Title: StrictStr | None = None
    KBId: StrictStr | None = None
    Classification: StrictStr | None = None
    Severity: StrictStr | None = None
    State: StrictStr | None = None
    InstalledTime: datetime.datetime | StrictStr | None = None
    CVEIds: StrictStr | None = None
