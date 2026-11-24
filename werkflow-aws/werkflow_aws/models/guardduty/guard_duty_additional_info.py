from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyAdditionalInfo(BaseModel):
    VersionId: StrictStr | None = None
    DeviceName: StrictStr | None = None
