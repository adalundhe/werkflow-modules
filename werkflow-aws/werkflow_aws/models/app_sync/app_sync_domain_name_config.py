from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncDomainNameConfig(BaseModel):
    domainName: StrictStr | None = None
    description: StrictStr | None = None
    certificateArn: StrictStr | None = None
    appsyncDomainName: StrictStr | None = None
    hostedZoneId: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    domainNameArn: StrictStr | None = None
