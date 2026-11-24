from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_flywheel_filter import ComprehendFlywheelFilter


class ComprehendListFlywheelsRequest(BaseModel):
    Filter: ComprehendFlywheelFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
