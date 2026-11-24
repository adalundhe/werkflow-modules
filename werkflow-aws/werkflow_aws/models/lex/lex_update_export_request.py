from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexUpdateExportRequest(BaseModel):
    exportId: StrictStr
    filePassword: StrictStr | None = None
