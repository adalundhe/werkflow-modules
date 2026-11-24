from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SESResourceTenantMetadata(BaseModel):
    TenantName: StrictStr | None = None
    TenantId: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    AssociatedTimestamp: datetime.datetime | StrictStr | None = None
