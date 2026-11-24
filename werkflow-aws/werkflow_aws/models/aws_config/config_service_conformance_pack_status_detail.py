from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConfigServiceConformancePackStatusDetail(BaseModel):
    ConformancePackName: StrictStr | None = None
    ConformancePackId: StrictStr | None = None
    ConformancePackArn: StrictStr | None = None
    ConformancePackState: StrictStr | None = None
    StackArn: StrictStr | None = None
    ConformancePackStatusReason: StrictStr | None = None
    LastUpdateRequestedTime: datetime.datetime | StrictStr | None = None
    LastUpdateCompletedTime: datetime.datetime | StrictStr | None = None
    Type: StrictStr | None = None
