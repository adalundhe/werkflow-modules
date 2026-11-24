from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RDSModifyTenantDatabaseRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    TenantDBName: StrictStr
    MasterUserPassword: StrictStr | None = None
    NewTenantDBName: StrictStr | None = None
    ManageMasterUserPassword: StrictBool | None = None
    RotateMasterUserPassword: StrictBool | None = None
    MasterUserSecretKmsKeyId: StrictStr | None = None
