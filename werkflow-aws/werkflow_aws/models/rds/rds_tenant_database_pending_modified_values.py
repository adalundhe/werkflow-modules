from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSTenantDatabasePendingModifiedValues(BaseModel):
    MasterUserPassword: StrictStr | None = None
    TenantDBName: StrictStr | None = None
