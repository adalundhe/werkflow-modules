from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailPendingModifiedRelationalDatabaseValues(BaseModel):
    masterUserPassword: StrictStr | None = None
    engineVersion: StrictStr | None = None
    backupRetentionEnabled: StrictBool | None = None
