from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessDeleteGroupRequest(BaseModel):
    applicationId: StrictStr
    indexId: StrictStr
    groupName: StrictStr
    dataSourceId: StrictStr | None = None
