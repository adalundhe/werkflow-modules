from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneSubscribedProjectInput(BaseModel):
    identifier: StrictStr | None = None
