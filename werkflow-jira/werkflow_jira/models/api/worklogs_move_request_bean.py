from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class WorklogsMoveRequestBean(BaseModel):
    ids: list[StrictInt] | None = None
    issueIdOrKey: StrictStr | None = None
