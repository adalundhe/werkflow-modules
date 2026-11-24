from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RDSSourceRegion(BaseModel):
    RegionName: StrictStr | None = None
    Endpoint: StrictStr | None = None
    Status: StrictStr | None = None
    SupportsDBInstanceAutomatedBackupsReplication: StrictBool | None = None
