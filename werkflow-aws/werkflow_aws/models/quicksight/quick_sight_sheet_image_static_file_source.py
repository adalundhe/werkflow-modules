from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSheetImageStaticFileSource(BaseModel):
    StaticFileId: StrictStr | None = None
