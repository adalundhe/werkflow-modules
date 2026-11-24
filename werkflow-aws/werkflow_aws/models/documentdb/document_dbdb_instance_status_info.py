from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DocumentDBDBInstanceStatusInfo(BaseModel):
    StatusType: StrictStr | None = None
    Normal: StrictBool | None = None
    Status: StrictStr | None = None
    Message: StrictStr | None = None
