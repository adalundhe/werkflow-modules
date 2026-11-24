from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class DynamoDBVectorCapacity(BaseModel):
    VectorSearchRequestBytes: StrictFloat | StrictInt | None = None
    VectorWriteRequestBytes: StrictFloat | StrictInt | None = None
