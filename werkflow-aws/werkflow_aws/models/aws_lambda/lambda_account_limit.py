from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LambdaAccountLimit(BaseModel):
    TotalCodeSize: StrictInt | None = None
    CodeSizeUnzipped: StrictInt | None = None
    CodeSizeZipped: StrictInt | None = None
    ConcurrentExecutions: StrictInt | None = None
    UnreservedConcurrentExecutions: StrictInt | None = None
