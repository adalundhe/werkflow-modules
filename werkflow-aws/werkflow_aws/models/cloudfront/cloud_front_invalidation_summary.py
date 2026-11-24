from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudFrontInvalidationSummary(BaseModel):
    Id: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
