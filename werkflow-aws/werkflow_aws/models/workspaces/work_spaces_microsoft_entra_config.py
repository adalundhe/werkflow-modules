from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesMicrosoftEntraConfig(BaseModel):
    TenantId: StrictStr | None = None
    ApplicationConfigSecretArn: StrictStr | None = None
