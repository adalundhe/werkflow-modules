from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKPartitionSource(BaseModel):
    SourceName: StrictStr | None = None
