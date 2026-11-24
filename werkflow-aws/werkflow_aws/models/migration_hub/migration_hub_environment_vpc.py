from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class MigrationHubEnvironmentVpc(BaseModel):
    AccountId: StrictStr | None = None
    CidrBlocks: list[StrictStr] | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    EnvironmentId: StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    VpcId: StrictStr | None = None
    VpcName: StrictStr | None = None
