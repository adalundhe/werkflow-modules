from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueEdge(BaseModel):
    SourceId: StrictStr | None = None
    DestinationId: StrictStr | None = None
