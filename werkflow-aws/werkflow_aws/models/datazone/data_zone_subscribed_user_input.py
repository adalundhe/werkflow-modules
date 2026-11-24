from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneSubscribedUserInput(BaseModel):
    identifier: StrictStr | None = None
