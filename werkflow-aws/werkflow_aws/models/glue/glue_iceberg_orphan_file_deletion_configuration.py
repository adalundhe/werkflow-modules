from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueIcebergOrphanFileDeletionConfiguration(BaseModel):
    orphanFileRetentionPeriodInDays: StrictInt | None = None
    location: StrictStr | None = None
    runRateInHours: StrictInt | None = None
