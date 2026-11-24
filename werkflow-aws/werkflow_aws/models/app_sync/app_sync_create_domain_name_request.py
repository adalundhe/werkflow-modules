from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncCreateDomainNameRequest(BaseModel):
    domainName: StrictStr
    certificateArn: StrictStr
    description: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
