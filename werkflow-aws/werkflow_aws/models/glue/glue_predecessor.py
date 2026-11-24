from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GluePredecessor(BaseModel):
    JobName: StrictStr | None = None
    RunId: StrictStr | None = None
