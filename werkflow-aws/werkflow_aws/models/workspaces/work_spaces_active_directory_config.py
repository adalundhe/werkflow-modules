from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesActiveDirectoryConfig(BaseModel):
    DomainName: StrictStr | None = None
    ServiceAccountSecretArn: StrictStr | None = None
