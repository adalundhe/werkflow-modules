from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFRespondActivityTaskFailedRequest(BaseModel):
    taskToken: StrictStr
    reason: StrictStr | None = None
    details: StrictStr | None = None
