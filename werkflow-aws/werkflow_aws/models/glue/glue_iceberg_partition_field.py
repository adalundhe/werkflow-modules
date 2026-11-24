from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueIcebergPartitionField(BaseModel):
    SourceId: StrictInt | None = None
    Transform: StrictStr | None = None
    Name: StrictStr | None = None
    FieldId: StrictInt | None = None
