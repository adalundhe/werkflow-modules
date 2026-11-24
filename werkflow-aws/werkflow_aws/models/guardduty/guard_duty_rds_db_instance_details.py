from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_tag import GuardDutyTag


class GuardDutyRdsDbInstanceDetails(BaseModel):
    DbInstanceIdentifier: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    DbClusterIdentifier: StrictStr | None = None
    DbInstanceArn: StrictStr | None = None
    DbiResourceId: StrictStr | None = None
    Tags: list[GuardDutyTag] | None = None
