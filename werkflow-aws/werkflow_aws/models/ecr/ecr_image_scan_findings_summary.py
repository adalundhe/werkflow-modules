from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ECRImageScanFindingsSummary(BaseModel):
    imageScanCompletedAt: datetime.datetime | StrictStr | None = None
    vulnerabilitySourceUpdatedAt: datetime.datetime | StrictStr | None = None
    findingSeverityCounts: dict[StrictStr, StrictInt] | None = None
