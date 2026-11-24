from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SESRecommendation(BaseModel):
    ResourceArn: StrictStr | None = None
    Type: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    LastUpdatedTimestamp: datetime.datetime | StrictStr | None = None
    Impact: StrictStr | None = None
