from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerSqsQueueConfiguration(BaseModel):
    queuePolicy: StrictStr | None = None
