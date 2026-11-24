from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .swf_activity_type import SWFActivityType


class SWFDeprecateActivityTypeRequest(BaseModel):
    domain: StrictStr
    activityType: SWFActivityType
