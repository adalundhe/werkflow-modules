from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .swf_activity_type import SWFActivityType


class SWFActivityTypeInfo(BaseModel):
    activityType: SWFActivityType | None = None
    status: StrictStr | None = None
    description: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    deprecationDate: datetime.datetime | StrictStr | None = None
