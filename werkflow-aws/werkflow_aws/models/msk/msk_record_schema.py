from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKRecordSchema(BaseModel):
    GsrArn: StrictStr | None = None
