from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerDynamodbStreamConfiguration(BaseModel):
    streamPolicy: StrictStr | None = None
