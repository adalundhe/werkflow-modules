from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueDistributionData(BaseModel):
    BinEdges: list[StrictStr] | None = None
    Count: list[StrictInt] | None = None
    DataType: StrictStr | None = None
