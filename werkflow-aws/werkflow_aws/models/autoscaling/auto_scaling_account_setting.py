from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AutoScalingAccountSetting(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
    EnforcementType: StrictStr | None = None
    EnforcementDate: datetime.datetime | StrictStr | None = None
    DefaultValue: StrictStr | None = None
    EnforcedValue: StrictStr | None = None
