from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamWriteUpdateDatabaseRequest(BaseModel):
    DatabaseName: StrictStr
    KmsKeyId: StrictStr
