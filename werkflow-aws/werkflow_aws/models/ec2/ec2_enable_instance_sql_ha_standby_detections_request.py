from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2EnableInstanceSqlHaStandbyDetectionsRequest(BaseModel):
    InstanceIds: list[StrictStr]
    SqlServerCredentials: StrictStr | None = None
    DryRun: StrictBool | None = None
