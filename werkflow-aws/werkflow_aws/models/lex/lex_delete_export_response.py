from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class LexDeleteExportResponse(BaseModel):
    exportId: StrictStr | None = None
    exportStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
