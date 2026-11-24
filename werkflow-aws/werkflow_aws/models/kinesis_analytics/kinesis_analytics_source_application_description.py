from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisAnalyticsSourceApplicationDescription(BaseModel):
    ApplicationName: StrictStr | None = None
    ApplicationCreationTimestamp: datetime.datetime | StrictStr | None = None
    ApplicationVersionId: StrictInt | None = None
