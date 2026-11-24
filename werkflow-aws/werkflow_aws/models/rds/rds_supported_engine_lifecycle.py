from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class RDSSupportedEngineLifecycle(BaseModel):
    LifecycleSupportName: StrictStr | None = None
    LifecycleSupportStartDate: datetime.datetime | StrictStr | None = None
    LifecycleSupportEndDate: datetime.datetime | StrictStr | None = None
