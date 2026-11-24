from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GlueIcebergOptimizationPropertiesOutput(BaseModel):
    RoleArn: StrictStr | None = None
    Compaction: dict[StrictStr, StrictStr] | None = None
    Retention: dict[StrictStr, StrictStr] | None = None
    OrphanFileDeletion: dict[StrictStr, StrictStr] | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
