from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SESTenantInfo(BaseModel):
    TenantName: StrictStr | None = None
    TenantId: StrictStr | None = None
    TenantArn: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    SendingStatus: StrictStr | None = None
