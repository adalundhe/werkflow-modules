from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RDSDeleteTenantDatabaseRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    TenantDBName: StrictStr
    SkipFinalSnapshot: StrictBool | None = None
    FinalDBSnapshotIdentifier: StrictStr | None = None
