from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_tag import GuardDutyTag


class GuardDutyRdsLimitlessDbDetails(BaseModel):
    DbShardGroupIdentifier: StrictStr | None = None
    DbShardGroupResourceId: StrictStr | None = None
    DbShardGroupArn: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    DbClusterIdentifier: StrictStr | None = None
    Tags: list[GuardDutyTag] | None = None
