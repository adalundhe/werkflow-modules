from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class DetectiveDatasourcePackageUsageInfo(BaseModel):
    VolumeUsageInBytes: StrictInt | None = None
    VolumeUsageUpdateTime: datetime.datetime | StrictStr | None = None
