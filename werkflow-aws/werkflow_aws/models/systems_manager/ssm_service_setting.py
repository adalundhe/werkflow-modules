from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SSMServiceSetting(BaseModel):
    SettingId: StrictStr | None = None
    SettingValue: StrictStr | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
    LastModifiedUser: StrictStr | None = None
    ARN: StrictStr | None = None
    Status: StrictStr | None = None
