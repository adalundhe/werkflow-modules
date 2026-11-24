from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueSubObjectStatistics(BaseModel):
    SourceType: StrictStr | None = None
    GlueVersionId: StrictStr | None = None
    PartitionCount: StrictInt | None = None
    FileCount: StrictInt | None = None
    TotalFileBytes: StrictInt | None = None
