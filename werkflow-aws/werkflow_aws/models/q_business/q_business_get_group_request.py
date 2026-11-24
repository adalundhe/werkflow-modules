from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessGetGroupRequest(BaseModel):
    applicationId: StrictStr
    indexId: StrictStr
    groupName: StrictStr
    dataSourceId: StrictStr | None = None
