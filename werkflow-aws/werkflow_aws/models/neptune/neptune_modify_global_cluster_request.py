from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class NeptuneModifyGlobalClusterRequest(BaseModel):
    GlobalClusterIdentifier: StrictStr
    NewGlobalClusterIdentifier: StrictStr | None = None
    DeletionProtection: StrictBool | None = None
    EngineVersion: StrictStr | None = None
    AllowMajorVersionUpgrade: StrictBool | None = None
