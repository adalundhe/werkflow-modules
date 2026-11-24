from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class IoTStatistics(BaseModel):
    count: StrictInt | None = None
    average: StrictFloat | StrictInt | None = None
    sum: StrictFloat | StrictInt | None = None
    minimum: StrictFloat | StrictInt | None = None
    maximum: StrictFloat | StrictInt | None = None
    sumOfSquares: StrictFloat | StrictInt | None = None
    variance: StrictFloat | StrictInt | None = None
    stdDeviation: StrictFloat | StrictInt | None = None
