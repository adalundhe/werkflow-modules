from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QuickSightBrandSummary(BaseModel):
    Arn: StrictStr | None = None
    BrandId: StrictStr | None = None
    BrandName: StrictStr | None = None
    Description: StrictStr | None = None
    BrandStatus: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
