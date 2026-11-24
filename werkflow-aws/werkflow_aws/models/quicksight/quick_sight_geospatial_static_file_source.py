from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightGeospatialStaticFileSource(BaseModel):
    StaticFileId: StrictStr | None = None
