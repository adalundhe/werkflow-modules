from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DirectoryServiceLDAPSSettingInfo(BaseModel):
    LDAPSStatus: StrictStr | None = None
    LDAPSStatusReason: StrictStr | None = None
    LastUpdatedDateTime: datetime.datetime | StrictStr | None = None
