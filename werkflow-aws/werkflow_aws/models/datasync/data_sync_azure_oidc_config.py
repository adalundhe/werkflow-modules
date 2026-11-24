from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncAzureOidcConfig(BaseModel):
    TenantId: StrictStr | None = None
    ClientId: StrictStr | None = None
