from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueIcebergSortField(BaseModel):
    SourceId: StrictInt | None = None
    Transform: StrictStr | None = None
    Direction: StrictStr | None = None
    NullOrder: StrictStr | None = None
