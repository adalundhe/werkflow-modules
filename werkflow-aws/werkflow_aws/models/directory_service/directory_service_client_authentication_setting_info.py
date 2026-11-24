from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DirectoryServiceClientAuthenticationSettingInfo(BaseModel):
    Type: StrictStr | None = None
    Status: StrictStr | None = None
    LastUpdatedDateTime: datetime.datetime | StrictStr | None = None
