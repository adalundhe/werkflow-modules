from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueIcebergCompactionConfiguration(BaseModel):
    strategy: StrictStr | None = None
    minInputFiles: StrictInt | None = None
    deleteFileThreshold: StrictInt | None = None
