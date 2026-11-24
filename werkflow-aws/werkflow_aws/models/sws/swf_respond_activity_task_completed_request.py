from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFRespondActivityTaskCompletedRequest(BaseModel):
    taskToken: StrictStr
    result: StrictStr | None = None
