from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisAnalyticsApplicationSummary(BaseModel):
    ApplicationName: StrictStr | None = None
    ApplicationARN: StrictStr | None = None
    ApplicationStatus: StrictStr | None = None
    ApplicationVersionId: StrictInt | None = None
    RuntimeEnvironment: StrictStr | None = None
    ApplicationMode: StrictStr | None = None
