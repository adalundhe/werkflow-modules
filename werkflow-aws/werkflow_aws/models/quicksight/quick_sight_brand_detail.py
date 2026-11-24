from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_logo import QuickSightLogo


class QuickSightBrandDetail(BaseModel):
    BrandId: StrictStr | None = None
    Arn: StrictStr | None = None
    BrandStatus: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    VersionId: StrictStr | None = None
    VersionStatus: StrictStr | None = None
    Errors: list[StrictStr] | None = None
    Logo: QuickSightLogo | None = None
