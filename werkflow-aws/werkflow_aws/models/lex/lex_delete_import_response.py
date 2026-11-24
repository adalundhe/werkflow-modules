from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class LexDeleteImportResponse(BaseModel):
    importId: StrictStr | None = None
    importStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
