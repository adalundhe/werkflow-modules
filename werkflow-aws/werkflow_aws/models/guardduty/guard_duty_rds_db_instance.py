from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyRdsDbInstance(BaseModel):
    DbInstanceIdentifier: StrictStr | None = None
    DbClusterIdentifier: StrictStr | None = None
    DbInstanceArn: StrictStr | None = None
    DbiResourceId: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
