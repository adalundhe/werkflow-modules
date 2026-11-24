from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFTaskList(BaseModel):
    name: StrictStr | None = None
