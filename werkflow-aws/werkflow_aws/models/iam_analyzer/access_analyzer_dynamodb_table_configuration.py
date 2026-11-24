from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerDynamodbTableConfiguration(BaseModel):
    tablePolicy: StrictStr | None = None
