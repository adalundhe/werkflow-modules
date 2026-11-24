from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueIcebergOptimizationProperties(BaseModel):
    RoleArn: StrictStr | None = None
    Compaction: dict[StrictStr, StrictStr] | None = None
    Retention: dict[StrictStr, StrictStr] | None = None
    OrphanFileDeletion: dict[StrictStr, StrictStr] | None = None
