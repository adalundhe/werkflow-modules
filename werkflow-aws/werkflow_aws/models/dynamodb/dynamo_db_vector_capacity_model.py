from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class DynamoDBVectorCapacityModel(BaseModel):
    VectorSearchRequestBytes: StrictFloat | StrictInt | None = None
    VectorWriteRequestBytes: StrictFloat | StrictInt | None = None
