from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailUpdateRelationalDatabaseRequest(BaseModel):
    relationalDatabaseName: StrictStr
    masterUserPassword: StrictStr | None = None
    rotateMasterUserPassword: StrictBool | None = None
    preferredBackupWindow: StrictStr | None = None
    preferredMaintenanceWindow: StrictStr | None = None
    enableBackupRetention: StrictBool | None = None
    disableBackupRetention: StrictBool | None = None
    publiclyAccessible: StrictBool | None = None
    applyImmediately: StrictBool | None = None
    caCertificateIdentifier: StrictStr | None = None
    relationalDatabaseBlueprintId: StrictStr | None = None
