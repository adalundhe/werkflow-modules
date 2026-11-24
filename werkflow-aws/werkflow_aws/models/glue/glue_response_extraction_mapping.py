from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueResponseExtractionMapping(BaseModel):
    ContentPath: StrictStr | None = None
    HeaderKey: StrictStr | None = None
