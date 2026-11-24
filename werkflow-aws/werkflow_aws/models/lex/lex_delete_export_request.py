from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDeleteExportRequest(BaseModel):
    exportId: StrictStr
