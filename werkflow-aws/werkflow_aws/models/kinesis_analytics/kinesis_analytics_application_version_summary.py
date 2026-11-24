from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisAnalyticsApplicationVersionSummary(BaseModel):
    ApplicationVersionId: StrictInt | None = None
    ApplicationStatus: StrictStr | None = None
