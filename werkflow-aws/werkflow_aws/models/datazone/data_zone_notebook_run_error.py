from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneNotebookRunError(BaseModel):
    message: StrictStr | None = None
