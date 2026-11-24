from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehosePartitionField(BaseModel):
    SourceName: StrictStr | None = None
