from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFRespondActivityTaskCanceledRequest(BaseModel):
    taskToken: StrictStr
    details: StrictStr | None = None
