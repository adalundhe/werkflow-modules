from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisPartitionField(BaseModel):
    Transform: StrictStr | None = None
    SourceName: StrictStr | None = None
