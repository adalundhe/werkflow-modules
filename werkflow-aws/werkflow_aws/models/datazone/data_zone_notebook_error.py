from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneNotebookError(BaseModel):
    message: StrictStr | None = None
