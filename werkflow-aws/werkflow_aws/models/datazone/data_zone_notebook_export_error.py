from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneNotebookExportError(BaseModel):
    message: StrictStr | None = None
