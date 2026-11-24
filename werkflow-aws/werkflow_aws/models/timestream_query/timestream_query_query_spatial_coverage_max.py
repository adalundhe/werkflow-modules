from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class TimestreamQueryQuerySpatialCoverageMax(BaseModel):
    Value: StrictFloat | StrictInt | None = None
    TableArn: StrictStr | None = None
    PartitionKey: list[StrictStr] | None = None
