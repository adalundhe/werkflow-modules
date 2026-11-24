from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveUnprocessedGraph(BaseModel):
    GraphArn: StrictStr | None = None
    Reason: StrictStr | None = None
